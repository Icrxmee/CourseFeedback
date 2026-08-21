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
pesquisa = cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas)

quantidade_alunos = input("Digite quantos alunos irão responder a pesquisa:")

while True: 
    if quantidade_alunos.isdigit():
        quantidade_alunos = int(quantidade_alunos)
        break

    print("Opção inválida, escreva um valor numérico!")

coletar_respostas(quantidade_alunos, pesquisa)

gerar_relatorios(pesquisa, quantidade_alunos)
