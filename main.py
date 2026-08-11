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
    "perguntas": []
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
print(pesquisa)
        
