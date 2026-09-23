import json
import os
import shutil

ARQUIVO = "pesquisa.json"
ARQUIVO_EXEMPLO = "pesquisa_exemplo.json"


def existe_pesquisa():
    return os.path.exists(ARQUIVO)


def semear():
    """Primeira execução num ambiente novo: copia o exemplo.

    O cadastro de pesquisa ainda existe só no terminal. Um servidor
    recém-criado não tem terminal interativo — sem esta semente, o
    link público começaria numa tela vazia, sem relatório possível.
    """
    if not existe_pesquisa() and os.path.exists(ARQUIVO_EXEMPLO):
        shutil.copyfile(ARQUIVO_EXEMPLO, ARQUIVO)


def salvar_pesquisa(pesquisa):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(pesquisa, arquivo, ensure_ascii=False, indent=4)


def carregar_pesquisa():
    with open(ARQUIVO, encoding="utf-8") as arquivo:
        return json.load(arquivo)
