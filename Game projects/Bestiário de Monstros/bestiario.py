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
    print("\n===== Novo Monstro =====")

    nome = input("Nome: ").strip()

    tipo = input("Tipo: ").strip()

    hp = int(input("HP: "))

    ataque = int(input("Ataque: "))

    defesa = int(input("Defesa: "))

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
Ataque: {m["Ataque"]}
Defesa: {m["Defesa"]}
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

    tipo = input("Tipo").strip().lower()

    encontrados = False

    for m in monstros:

        if m["Tipo"].lower() == tipo:

            print(f'-{m["Nome"]}')

            encontrados = True

    if not encontrados:
        print("Nenhum monstro encontrado.")

#Editar

def editar(monstros):

    nome = input("Nome do monstro: ").strip().lower()

    for m in monstros:

        if m["Nome"].lower() == nome:

            print("Deixe vazio para manter o valor.")

            novo = input(f'Novo HP ({m["HP"]}): ')

            if novo:
                m["HP"] = int(novo)

            novo = input(f'Novo ataque ({m["Ataque"]}): ')

            if novo:
                m["Ataque"] = int(novo)

            novo = input(f'Nova defesa ({m["Defesa"]}):')

            if novo:
                m["Defesa"] = int(novo)

            salvar(monstros)

            print("Monstro atualizado com sucesso!")

            return

    print("Monstro não encontrado.")

#Excluir

def excluir(monstros):

    nome = input("Nome do monstro: ").strip().lower()

    for m in monstros:

        if m["Nome"].lower() == nome:

            monstros.remove(m)

            salvar(monstros)

            print("Monstro removido.")

            return

    print("Monstro não encontrado.")

#Menu

def menu():

    monstros = carregar()

    while True:

        print("""
===== Bestiário =====
1 - Registrar monstro
2 - Listar monstros
3 - Buscar por nome
4 - Filtrar por tipo
5 - Editar
6 - Excluir
0 - Sair
""")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            registrar(monstros)

        elif opcao == "2":
            listar(monstros)

        elif opcao == "3":
            buscar(monstros)

        elif opcao == "4":
            filtrar(monstros)

        elif opcao == "5":
            editar(monstros)

        elif opcao == "6":
            excluir(monstros)

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Erro,opção inválida!")

menu()