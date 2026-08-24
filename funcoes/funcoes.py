def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)

def cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas):

    for i in range(quantidade_perguntas):
        print(f"Pergunta {i + 1}:")
        texto_pergunta = input("Escreva a pergunta que deseja fazer: ")

        print("Tipos de Perguntas")

        for numero, tipo in tipo_perguntas.items():
            print(f"{numero} {tipo['nome']}")

        while True:
            tipo = input("Selecione o número do tipo:")

            if tipo in tipo_perguntas:
                break
            print("Opção inválida, tente novamente!")
    
        tipo = tipo_perguntas[tipo]
        pergunta = {
                "texto": texto_pergunta,
                "tipo": tipo
                            }
        pesquisa['perguntas'].append(pergunta)
    return pesquisa

def coletar_respostas(quantidade_alunos, pesquisa ):

        for i in range(quantidade_alunos):
            nome = input("Digite seu nome: ")
            respostas_aluno = []

            for numero_pergunta, pergunta in enumerate(pesquisa['perguntas'], start=1):
                print(f'Pergunta {numero_pergunta}:')
                print(f"{pergunta["texto"]}")

                percorrer_opcoes = pergunta["tipo"]["opcoes"]
                print(f"Opções:")

                for numero_opcao, opcao in enumerate(percorrer_opcoes, start=1):
                    print(f"{numero_opcao}. {opcao}")

                while True:
                    resposta_aluno = input("Selecione sua resposta:")

                    if resposta_aluno.isdigit():
                        indice = int(resposta_aluno) - 1

                        if 0 <= indice < len(percorrer_opcoes):
                            break
                
                    print("Opção inválida, tente novamente!")

                resposta = percorrer_opcoes[indice]

                resposta_aluno = {
                    "nome": nome,
                    "pergunta": numero_pergunta,
                    "resposta": resposta
                }

                respostas_aluno.append(resposta_aluno)

            pesquisa["respostas"].append(respostas_aluno)

        return pesquisa
            
def gerar_relatorios(pesquisa, quantidade_alunos):

    for numero_pergunta, pergunta in enumerate(pesquisa["perguntas"], start=1):

        contadores = contar_respostas(pergunta, numero_pergunta, pesquisa['respostas'])     

        if pergunta['tipo']['nome'] == 'Sim_Nao':

            porcentagem_sim = (contadores["Sim"] / quantidade_alunos) * 100
            porcentagem_nao = (contadores["Não"] / quantidade_alunos) * 100

            print(f"pergunta: {pergunta['texto']}")
            print(f"Sim: {contadores["Sim"]} ({porcentagem_sim:.1f}%)")
            print(f"Não: {contadores["Não"]} ({porcentagem_nao:.1f}%)")

        elif pergunta['tipo']['nome'] == 'Nota':

            print(f"pergunta: {pergunta['texto']}")

            for nota in pergunta['tipo']["opcoes"]:

                porcentagem = (contadores[nota] / quantidade_alunos ) * 100

                print(
                    f"Nota {nota}: "
                    f"{contadores[nota]} "
                    f"({porcentagem:.1f}%)"
                )

def contar_respostas(pergunta, numero_pergunta, respostas):

    contadores = {}

    for opcao in pergunta["tipo"]["opcoes"]:
        contadores[opcao] = 0 

    for respostas_aluno in respostas:

        for resposta in respostas_aluno:

            if resposta["pergunta"] == numero_pergunta:

                contadores[resposta["resposta"]] += 1 


    return contadores

    