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

#Registrar

def registrar(personagens):

    print("\n===== Novo Personagem =====")

    nome = input("Nome: ").strip()
    obra = input("Obra: ").strip()
    especie = input("Espécie: ").strip()
    genero = input("Gênero: ").strip()
    idade  = input("Idade: ").strip()
    ocupacao = input("Ocupação: ").strip()
    personalidade = input("Personalidade: ").strip()
    habilidade = input("Habilidade: ").strip()
    descricao = input("Descrição: ").strip()

    personagem = {
        "Nome": nome,
        "Obra": obra,
        "Espécie": especie,
        "Gênero": genero,
        "Idade": idade,
        "Ocupação": ocupacao,
        "Personalidade": personalidade,
        "Habilidade": habilidade,
        "Descrição": descricao
    }

    personagens.append(personagem)

    salvar(personagens)

    print("\nPersonagem cadastrado com sucesso!")

#Listar

def listar(personagens):

    if not personagens:
        print("\nNenhum personagem registrado.")
        return

    print("\n===== Enciclopédia =====")

    for i,personagem in enumerate(personagens, start=1):

        print(f"""
{i}. {personagem["Nome"]}
Obra: {personagem["Obra"]}
Espécie: {personagem["Espécie"]}
Gênero: {personagem["Gênero"]}
Idade: {personagem["Idade"]}
Ocupação: {personagem["Ocupação"]}
Personalidade: {personagem["Personalidade"]}
Habilidade: {personagem["Habilidade"]}
Descrição: {personagem["Descrição"]}
""")