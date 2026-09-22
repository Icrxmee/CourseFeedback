import json
import os

ARQUIVO = "pesquisa.json"


def existe_pesquisa():
    return os.path.exists(ARQUIVO)


def salvar_pesquisa(pesquisa):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(pesquisa, arquivo, ensure_ascii=False, indent=4)


def carregar_pesquisa():
    with open(ARQUIVO, encoding="utf-8") as arquivo:
        return json.load(arquivo)
