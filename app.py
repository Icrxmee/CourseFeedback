from flask import Flask, render_template

import funcoes.persistencia as persistencia

app = Flask(__name__)


@app.route("/")
def inicio():
    pesquisa = None

    if persistencia.existe_pesquisa():
        pesquisa = persistencia.carregar_pesquisa()

    return render_template("index.html", pesquisa=pesquisa)


if __name__ == "__main__":
    # debug=True apenas em desenvolvimento: recarrega ao salvar e mostra erros
    app.run(debug=True, port=5000)
