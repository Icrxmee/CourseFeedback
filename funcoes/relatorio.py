import funcoes.processamento as processamento

def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)

def gerar_relatorios(pesquisa, quantidade_alunos):

    for pergunta in (pesquisa["perguntas"]):

        contadores = processamento.contar_respostas(pergunta, pesquisa['respostas'])
        porcentagens = processamento.calcular_porcentagem(contadores, quantidade_alunos)
        rotulo = pergunta['tipo'].get('rotulo', '')

        print(f"pergunta: {pergunta['texto']}")

        for opcao in pergunta['tipo']['opcoes']:

            etiqueta = f"{rotulo} {opcao}" if rotulo else str(opcao)

            print(f"{etiqueta}: {contadores[opcao]} ({porcentagens[opcao]:.1f}%)")
