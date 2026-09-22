import funcoes.processamento as processamento

def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)

def gerar_relatorios(pesquisa, quantidade_alunos):

    for pergunta in (pesquisa["perguntas"]):

        print(f"pergunta: {pergunta['texto']}")

        if pergunta['tipo'].get('resposta_livre'):

            for resposta in processamento.filtrar_respostas(pergunta, pesquisa['respostas']):
                print(f"- {resposta['nome']}: {resposta['resposta']}")

        else:

            contadores = processamento.contar_respostas(pergunta, pesquisa['respostas'])
            porcentagens = processamento.calcular_porcentagem(contadores, quantidade_alunos)
            rotulo = pergunta['tipo'].get('rotulo', '')

            for opcao in pergunta['tipo']['opcoes']:

                etiqueta = f"{rotulo} {opcao}" if rotulo else str(opcao)

                print(f"{etiqueta}: {contadores[opcao]} ({porcentagens[opcao]:.1f}%)")
