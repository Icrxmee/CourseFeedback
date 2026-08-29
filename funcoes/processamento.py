def contar_respostas(pergunta, numero_pergunta, respostas):

    contadores = {}

    for opcao in pergunta["tipo"]["opcoes"]:
        contadores[opcao] = 0 

    for respostas_aluno in respostas:

        for resposta in respostas_aluno:

            if resposta["pergunta"] == numero_pergunta:

                contadores[resposta["resposta"]] += 1 


    return contadores

def calcular_porcentagem(contadores, quantidade_alunos):

    porcentagens = {}

    for opcao, quantidade in contadores.items():

        porcentagem = (quantidade / quantidade_alunos) * 100

        porcentagens[opcao] = porcentagem

    return porcentagens