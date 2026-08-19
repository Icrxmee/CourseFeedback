def tela_inicial_terminal():
    print("=" * 40)
    print("SISTEMA DE AVALIAÇÃO DE CURSO")
    print("=" * 40)

def cadastro_perguntas(quantidade_perguntas, pesquisa, tipo_perguntas):

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
    return pesquisa