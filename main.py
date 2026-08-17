from funcoes.funcoes import *

tipo_perguntas = {
    '1': {'nome':'Sim_Nao',
          'opcoes': ['Sim', 'Não']},

    '2': {'nome': 'Nota',
          'opcoes': [1,2,3,4,5]}
}

tela_inicial_terminal()

curso = input("Nome do Curso:")
professor = input("Nome do Professor:")

pesquisa = {
    "curso": curso,
    "professor": professor,
    "perguntas": [],
    "respostas": []
}

quantidade_perguntas = int(input("Digite quantas perguntas deseja realizar: "))

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

while True:
    quantidade_alunos = input("Digite quantos alunos irão responder a pesquisa:")

    if quantidade_alunos.isdigit():
        quantidade_alunos = int(quantidade_alunos)
        break
    print("Opção inválida, escreva um valor numérico!")

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


for numero_pergunta, pergunta in enumerate(pesquisa["perguntas"], start=1):

    contador_sim = 0
    contador_não = 0
    nota_1 = 0
    nota_2 = 0
    nota_3 = 0
    nota_4 = 0
    nota_5 = 0

    for respostas_aluno in pesquisa["respostas"]:

        for resposta in respostas_aluno:

            if pergunta['tipo']['nome'] == "Sim_Nao":

                if resposta["pergunta"] == numero_pergunta:
                    
                    if resposta["resposta"] == "Sim":
                        contador_sim += 1

                    if resposta["resposta"] == "Não":
                        contador_não += 1

            if pergunta['tipo']['nome'] == 'Nota':

                if resposta["pergunta"] == numero_pergunta:

                    if resposta["resposta"] == 1:
                        nota_1 += 1

                    if resposta["resposta"] == 2:
                        nota_2 += 1

                    if resposta["resposta"] == 3:
                        nota_3 += 1

                    if resposta["resposta"] == 4:
                        nota_4 += 1

                    if resposta["resposta"] == 5:
                        nota_5 += 1


    if pergunta['tipo']['nome'] == 'Sim_Nao':

        porcentagem_sim = (contador_sim / quantidade_alunos) * 100
        porcentagem_nao = (contador_não / quantidade_alunos) * 100

        print(f"pergunta: {pergunta['texto']}")
        print(f"Sim: {contador_sim} ({porcentagem_sim:.1f}%)")
        print(f"Não: {contador_não} ({porcentagem_nao:.1f}%)")

    elif pergunta['tipo']['nome'] == 'Nota':

        porcentagem_nota1 = (nota_1 / quantidade_alunos) * 100
        porcentagem_nota2 = (nota_2 / quantidade_alunos) * 100
        porcentagem_nota3 = (nota_3 / quantidade_alunos) * 100
        porcentagem_nota4 = (nota_4 / quantidade_alunos) * 100
        porcentagem_nota5 = (nota_5 / quantidade_alunos) * 100

        print(f"Nota 1: {nota_1} ({porcentagem_nota1:.1f}%)")
        print(f"Nota 2: {nota_2} ({porcentagem_nota2:.1f}%)")
        print(f"Nota 3: {nota_3} ({porcentagem_nota3:.1f}%)")
        print(f"Nota 4: {nota_4} ({porcentagem_nota4:.1f}%)")
        print(f"Nota 5: {nota_5} ({porcentagem_nota5:.1f}%)")