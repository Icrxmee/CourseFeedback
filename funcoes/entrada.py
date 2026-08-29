def solicitar_numero(mensagem):

    while True:

        valor = input(mensagem)

        if valor.isdigit():

            valor = int(valor)

            if valor > 0:

                return valor

        print("Opção inválida! Escreva um número maior que zero.")

def solicitar_texto(mensagem):

    while True:

        texto = input(mensagem)

        if texto.strip():
            return texto

        print("Opção inválida! Esse campo não pode ficar vazio.")

def cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas):

    for i in range(quantidade_perguntas):
        print(f"Pergunta {i + 1}:")
        texto_pergunta = solicitar_texto("Escreva a pergunta que deseja fazer: ")

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