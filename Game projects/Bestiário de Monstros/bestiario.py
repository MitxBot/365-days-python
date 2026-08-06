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

#Listar

def listar(monstros):

    if not monstros:

        print("\nNenhum monstro registrado.\n")
        return

    print("\n=== Bestiário ===")

    for i,m in enumerate(monstros,start=1):

        print(f"""
{i}.{m["Nome"]}
Tipo: {m["Tipo"]}
HP: {m["HP"]}
Ataque: {m["ATK"]}
Defesa: {m["DEF"]}
Habilidade: {m["Habilidade"]}
Rank: {m["Rank"]}
Descrição: {m["Descrição"]}
""")

#Buscar

def buscar(monstros):

    nome = input("Nome do Monstro: ").strip().lower()

    for m in monstros:

        if m["Nome"].lower() == nome:

            print("\nMonstro encontrado!\n")

            for chave,valor in m.items():

                print(f"{chave}:{valor}")

            return

    print("Monstro não encontrado.")

#Filtrar

def filtrar(monstros):

    tipo = input("Tipo: ").strip().lower()

    encontrados = False

    for m in monstros:

        if m["Tipo: "].lower() == tipo:

            print(f'-{m["Nome:"]}')

            encontrados = True

    if not encontrados:
        print("Nenhum encontrado.")