import os
import threading

from flask import Flask, render_template, request, redirect, url_for

import funcoes.persistencia as persistencia
import funcoes.relatorio as relatorio

app = Flask(__name__)

# Garante que "ler - anexar - salvar" aconteça por vez, sem
# duas respostas simultâneas se sobrescreverem.
_trava = threading.Lock()


@app.route("/")
def inicio():
    pesquisa = None

    if persistencia.existe_pesquisa():
        pesquisa = persistencia.carregar_pesquisa()

    return render_template("index.html", pesquisa=pesquisa)


@app.route("/responder")
def responder():
    if not persistencia.existe_pesquisa():
        return redirect(url_for("inicio"))

    pesquisa = persistencia.carregar_pesquisa()
    return render_template("responder.html", pesquisa=pesquisa, erros=[], form={})


@app.route("/responder", methods=["POST"])
def enviar_resposta():
    if not persistencia.existe_pesquisa():
        return redirect(url_for("inicio"))

    pesquisa = persistencia.carregar_pesquisa()
    erros, respostas_aluno = _validar(request.form, pesquisa)

    if erros:
        return render_template(
            "responder.html", pesquisa=pesquisa, erros=erros, form=request.form
        ), 400

    with _trava:
        pesquisa = persistencia.carregar_pesquisa()
        pesquisa["respostas"].append(respostas_aluno)
        persistencia.salvar_pesquisa(pesquisa)

    return redirect(url_for("obrigado"))


@app.route("/relatorio")
def relatorio_web():
    if not persistencia.existe_pesquisa():
        return redirect(url_for("inicio"))

    pesquisa = persistencia.carregar_pesquisa()
    secoes = relatorio.montar_relatorio(pesquisa)

    return render_template("relatorio.html", pesquisa=pesquisa, secoes=secoes)


@app.route("/obrigado")
def obrigado():
    return render_template("obrigado.html")


def _validar(form, pesquisa):
    """Confere o formulário no servidor. Devolve (erros, respostas_validas)."""
    erros = []
    respostas_aluno = []

    nome = form.get("nome", "").strip()
    if not nome:
        erros.append("Digite seu nome.")

    for pergunta in pesquisa["perguntas"]:
        valor = form.get(f"p_{pergunta['id']}")

        if pergunta["tipo"].get("resposta_livre"):
            respostas_aluno.append({
                "nome": nome,
                "pergunta": pergunta["id"],
                "resposta": valor if valor is not None else "",
            })
            continue

        opcoes = pergunta["tipo"]["opcoes"]

        if valor is None:
            erros.append(f"Responda: {pergunta['texto']}")
            continue

        if not valor.isdigit():
            erros.append(f"Resposta inválida: {pergunta['texto']}")
            continue

        indice = int(valor) - 1
        if not 0 <= indice < len(opcoes):
            erros.append(f"Resposta inválida: {pergunta['texto']}")
            continue

        respostas_aluno.append({
            "nome": nome,
            "pergunta": pergunta["id"],
            "resposta": opcoes[indice],
        })

    return erros, respostas_aluno


if __name__ == "__main__":
    # Produção NUNCA usa debug: o console do Werkzeug é de execução remota.
    # Desenvolvimento: FLASK_DEBUG=1 python app.py
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    porta = int(os.environ.get("PORT", "5000"))
    host = os.environ.get("HOST", "127.0.0.1")

    app.run(host=host, port=porta, debug=debug)
