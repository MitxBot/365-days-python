import json
import os

ARQUIVO = "monstros.json"

#Salvar e carregar

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO,"r",encoding="utf-8") as f:
            return json.load(f)
        return []

def salvar(monstros):
    with open(ARQUIVO,"w",encoding="utf-8") as f:
        json.dump(monstros,f,indent=4,ensure_ascii=False)

#Registrar

def registrar(monstros):
    print("\n=== Novo Monstro ===")

    nome = input("Nome: ").strip()

    tipo = input("Tipo: ").strip()

    hp = int(input("HP: "))

    ataque = int(input("ATk: "))

    defesa = int(input("DEF: "))

    habilidade = input("Habilidade: ").strip()

    rank = input("Rank: ").strip()

    descricao = input("Descrição: ").strip()

    monstro = {
        "Nome": nome,
        "Tipo": tipo,
        "HP": hp,
        "Ataque": ataque,
        "Defesa": defesa,
        "Habilidade": habilidade,
        "Rank": rank,
        "Descrição": descricao
    }

    monstros.append(monstro)

    salvar(monstros)

    print("\nMonstro registrado com sucesso!\n")