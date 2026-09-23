import funcoes.entrada as entrada 
import funcoes.relatorio as relatorio
import funcoes.configuracao as configuracao
import funcoes.persistencia as persistencia

tipo_perguntas = configuracao.tipo_perguntas

relatorio.tela_inicial_terminal()

pesquisa = None

if persistencia.existe_pesquisa():
    print("1 - Continuar pesquisa salva")
    print("2 - Criar nova pesquisa")

    while True:
        opcao = input("Escolha uma opção: ")
        if opcao in ['1', '2']:
            break
        print("Opção inválida, tente novamente!")

    if opcao == '1':
        pesquisa = persistencia.carregar_pesquisa()

if pesquisa is None:
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

    persistencia.salvar_pesquisa(pesquisa)
    print(f"Pesquisa salva em {persistencia.ARQUIVO}.")

relatorio.gerar_relatorios(pesquisa)
