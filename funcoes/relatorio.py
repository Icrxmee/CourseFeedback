import funcoes.processamento as processamento


def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)


def montar_relatorio(pesquisa):
    """Monta o modelo de dados do relatorio (sem imprimir nada).

    Devolve uma lista de secoes, uma por pergunta:

    - pergunta fechada -> {"pergunta", "modo": "contagem", "linhas": [...]}
    - pergunta aberta  -> {"pergunta", "modo": "texto", "respostas": [...]}

    O terminal e a web consomem este mesmo modelo e apenas o apresentam
    do seu jeito (print ou HTML).
    """
    quantidade_alunos = len(pesquisa["respostas"])  # derivado, nao repetido
    secoes = []

    for pergunta in pesquisa["perguntas"]:

        if pergunta["tipo"].get("resposta_livre"):
            respostas = []

            for resposta in processamento.filtrar_respostas(
                pergunta, pesquisa["respostas"]
            ):
                respostas.append(
                    {"nome": resposta["nome"], "resposta": resposta["resposta"]}
                )

            secoes.append({"pergunta": pergunta, "modo": "texto", "respostas": respostas})

        else:
            contadores = processamento.contar_respostas(
                pergunta, pesquisa["respostas"]
            )
            porcentagens = processamento.calcular_porcentagem(
                contadores, quantidade_alunos
            )
            rotulo = pergunta["tipo"].get("rotulo", "")
            linhas = []

            for opcao in pergunta["tipo"]["opcoes"]:
                etiqueta = f"{rotulo} {opcao}" if rotulo else str(opcao)
                linhas.append(
                    {
                        "etiqueta": etiqueta,
                        "contagem": contadores[opcao],
                        "porcentagem": porcentagens[opcao],
                    }
                )

            secoes.append(
                {"pergunta": pergunta, "modo": "contagem", "linhas": linhas}
            )

    return secoes


def gerar_relatorios(pesquisa):
    """Apresenta o relatorio no terminal (uma apresentacao do modelo)."""
    for secao in montar_relatorio(pesquisa):

        print(f"pergunta: {secao['pergunta']['texto']}")

        if secao["modo"] == "texto":

            for resposta in secao["respostas"]:
                print(f"- {resposta['nome']}: {resposta['resposta']}")

        else:

            for linha in secao["linhas"]:
                print(
                    f"{linha['etiqueta']}: {linha['contagem']} "
                    f"({linha['porcentagem']:.1f}%)"
                )
