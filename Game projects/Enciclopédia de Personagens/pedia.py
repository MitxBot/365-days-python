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

#Buscar por Nome

def buscar(personagens):

    pesquisa = input("\nDigite o nome: ").strip().lower()

    encontrados = []

    for personagem in personagens:

        if pesquisa in personagem["Nome"].lower():
            encontrados.append(personagem)

    if not encontrados:
            print("\nNenhum personagem encontrado.")
            return

    print("\n===== Resultados =====")

    for personagem in encontrados:

        print(f"""
Nome: {personagem["Nome"]}
Obra: {personagem["Obra"]}
Espécie: {personagem["Espécie"]}
Gênero: {personagem["Gênero"]}
Idade: {personagem["Idade"]}
Ocupação: {personagem["Ocupação"]}
Personalidade: {personagem["Personalidade"]}
Habilidade: {personagem["Habilidade"]}
Descrição: {personagem["Descrição"]}
""")

#Filtrar por Obra

def filtrar_obar(personagens):

    obra = input("Digite a obra").strip().lower()

    encontrados = []
    
    for personagem in personagens:
    
        if personagem["Obra"].lower() == obra:
            encontrados.append(personagem)
    
    if not encontrados:
        print("\nNenhum personagem encontrado nessa obra.")
        return
    
    print("\n===== Personagens =====")
    
    for personagem in encontrados:
        print(f"- {personagem['Nome']}")

#Filtrar por Espécies

def filtrar_especie(personagens):

    especie = input("\nDigite a espécie: ").strip().lower()

    encontrados = []
        
    for personagem in personagens:
        
        if personagem["Espécie"].lower() == especie:
            encontrados.append(personagem)
        
    if not encontrados:
        print("\nNenhum personagem encontrado.")
        return
        
    print("\n===== Personagens =====")
        
    for personagem in encontrados:
        print(f"- {personagem['Nome']}")

#Editar

def editar(personagens):

    pesquisa = input("Digite o nome do personagem: ").strip().lower()

    for personagem in personagens:

        if personagem["Nome"].lower() == pesquisa:

            print("\nDeixe vazio para manter o valor atual.")

            novo_nome = input(
                f"Nome: ({personagem['Nome']}): "
            )

            if novo_nome:
                personagem["Nome"] = novo_nome

            nova_obra = input(
                f"Obra: ({personagem['Obra']}): "
            )

            if nova_obra:
                personagem["Obra"] = nova_obra

            nova_especie = input(
                f"Espécie: ({personagem['Espécie']}): "
            )

            if nova_especie:
                personagem["Espécie"] = nova_especie

            novo_genero = input(
                f"Gênero: ({personagem['Gênero']}): "
            )

            if novo_genero:
                personagem["Gênero"] = novo_genero

            nova_idade = input(
                f"Idade: ({personagem['Idade']}): "
            )

            if nova_idade:
                personagem["Idade"] = nova_idade

            nova_ocupacao = input(
                f"Ocupação: ({personagem['Ocupação']}): "
            )

            if nova_ocupacao:
                personagem["Ocupação"] = nova_ocupacao

            nova_personalidade = input(
                f"Pesonalidade: ({personagem['Personalidade']}): "
            )

            if nova_personalidade:
                personagem["Personalidade"] = nova_personalidade

            nova_habilidade = input(
                f"Habilidade: ({personagem['Habilidade']}): "
            )

            if nova_habilidade:
                personagem["Habilidade"] = nova_habilidade

            nova_descricao = input(
                f"Descrição: ({personagem['Descrição']}): "
            )

            if nova_descricao:
                personagem["Descrição"] = nova_descricao

            salvar(personagens)

            print("\nPersonagem atualizado!")

            return
    print("\nPersonagem não encontrado.")