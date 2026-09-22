def filtrar_respostas(pergunta, respostas):

    filtradas = []

    for respostas_aluno in respostas:

        for resposta in respostas_aluno:

            if resposta["pergunta"] == pergunta["id"]:

                filtradas.append(resposta)

    return filtradas

def contar_respostas(pergunta, respostas):

    contadores = {}

    for opcao in pergunta["tipo"]["opcoes"]:
        contadores[opcao] = 0 

    for resposta in filtrar_respostas(pergunta, respostas):

        contadores[resposta["resposta"]] += 1 


    return contadores

def calcular_porcentagem(contadores, quantidade_alunos):

    porcentagens = {}

    for opcao, quantidade in contadores.items():

        porcentagem = (quantidade / quantidade_alunos) * 100

        porcentagens[opcao] = porcentagem

    return porcentagens