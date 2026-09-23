from flask import Flask

import funcoes.persistencia as persistencia

app = Flask(__name__)


@app.route("/")
def inicio():
    if persistencia.existe_pesquisa():
        pesquisa = persistencia.carregar_pesquisa()
        resumo = (
            f"Curso: {pesquisa['curso']} | "
            f"Professor: {pesquisa['professor']} | "
            f"Perguntas: {len(pesquisa['perguntas'])} | "
            f"Respostas de alunos: {len(pesquisa['respostas'])}"
        )
    else:
        resumo = ("Nenhuma pesquisa criada ainda. "
                  "Crie uma pelo terminal: python main.py")

    return (
        "<h1>CourseFeedback</h1>"
        "<p>Sistema de avaliação de curso</p>"
        f"<p>{resumo}</p>"
    )


if __name__ == "__main__":
    # debug=True apenas em desenvolvimento: recarrega ao salvar e mostra erros
    app.run(debug=True, port=5000)
