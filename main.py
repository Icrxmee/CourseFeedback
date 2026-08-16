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

contador = 0

for respostas_aluno in pesquisa["respostas"]:

    for resposta in respostas_aluno:
        if resposta["resposta"] == "Sim":
            contador += 1
