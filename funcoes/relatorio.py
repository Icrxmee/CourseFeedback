import funcoes.processamento as processamento

def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)
            
def gerar_relatorios(pesquisa, quantidade_alunos):

    for numero_pergunta, pergunta in enumerate(pesquisa["perguntas"], start=1):

        contadores = processamento.contar_respostas(pergunta, numero_pergunta, pesquisa['respostas'])     


        if pergunta['tipo']['nome'] == 'Sim_Nao':

            porcentagens = processamento.calcular_porcentagem(contadores, quantidade_alunos)

            print(f"pergunta: {pergunta['texto']}")

            print(f"Sim: {contadores['Sim']}"
            f"({porcentagens['Sim']:.1f}%)")

            print(f"Não: {contadores['Não']}"
            f"({porcentagens['Não']:.1f}%)")

        elif pergunta['tipo']['nome'] == 'Nota':

            porcentagens = processamento.calcular_porcentagem(contadores, quantidade_alunos)

            print(f"pergunta: {pergunta['texto']}")

            for nota in pergunta['tipo']["opcoes"]:

                print(
                    f"Nota {nota}: "
                    f"{contadores[nota]} "
                    f"({porcentagens[nota]:.1f}%)"
                )

