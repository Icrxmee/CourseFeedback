from funcoes.entrada import *  
from funcoes.relatorio import *

tipo_perguntas = {
    '1': {'nome':'Sim_Nao',
          'opcoes': ['Sim', 'Não']},

    '2': {'nome': 'Nota',
          'opcoes': [1,2,3,4,5]}
}

tela_inicial_terminal()

curso = solicitar_texto("Nome do Curso: ")
professor = solicitar_texto("Nome do Professor: ")

pesquisa = {
    "curso": curso,
    "professor": professor,
    "perguntas": [],
    "respostas": []
}

quantidade_perguntas = solicitar_numero("Digite quantas perguntas deseja realizar: ")
pesquisa = cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas)

quantidade_alunos = solicitar_numero("Digite quantos alunos irão responder a pesquisa: ")

coletar_respostas(quantidade_alunos, pesquisa)

gerar_relatorios(pesquisa, quantidade_alunos)
