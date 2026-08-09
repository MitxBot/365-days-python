import json
import os

ARQUIVO = "personagem.json"

#Salvar e Carregar

def salvar(personagens):

    with open(ARQUIVO,"w",encoding="utf-8") as arquivo:
        json.dump(
            personagens,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def carregar():

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO,"r",encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []