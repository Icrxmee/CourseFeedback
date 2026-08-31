import funcoes.entrada as entrada 
import funcoes.relatorio as relatorio
import funcoes.configuracao as configuracao

tipo_perguntas = configuracao.tipo_perguntas

relatorio.tela_inicial_terminal()

curso = entrada.solicitar_texto("Nome do Curso: ")
professor = entrada.solicitar_texto("Nome do Professor: ")

pesquisa = {
    "curso": curso,
    "professor": professor,
    "perguntas": [],
    "respostas": []
}

quantidade_perguntas = entrada.solicitar_numero("Digite quantas perguntas deseja realizar: ")
pesquisa = entrada.cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas)

quantidade_alunos = entrada.solicitar_numero("Digite quantos alunos irão responder a pesquisa: ")

entrada.coletar_respostas(quantidade_alunos, pesquisa)

relatorio.gerar_relatorios(pesquisa, quantidade_alunos)
