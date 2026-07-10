import json
import os

ARQUIVO = "biblioteca.json"

#Carregar Banco de Dados

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    return []
        
#Salvar Banco de Dados

def salvar_dados(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros,arquivo,ensure_ascii=False,indent=4)

#Adicionar livros

def adicionar_livros(livros):
    titulo = input("Título: ").strip()

    if not titulo:
        print("Título inválido.")
        return

    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()

    livro = {
        "titulo" : titulo,
        "autor" : autor,
        "ano" : ano
    }

    livros.append(livro)
    salvar_dados(livros)

    print("Livro cadastrado com sucesso!")

#Listar livros

def listar_livros(livros):
    if not livros:
        print("\nNenhum livro cadastrado.")
        return
    
    print("\n=== Livros Cadastrados ===")

    for i, livro in enumerate(livros,start=1):
        print(f"""
Livro {i}
Título : {livro['titulo']}
Autor : {livro['autor']}
Ano : {livro['ano']}
""")

#Buscar livro

def buscar_livro(livros):
    busca = input("Digite o título do livro: ").strip().lower()

    encontrados = []

    for livro in livros:
        if busca in livro["titulo"].lower():
            encontrados.append(livro)

    if encontrados:
        print("\nResultados encontrados:\n")
        
        for livro in encontrados:
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano {livro['ano']}")
            print(f"-" * 30)

    else:
        print("Nenhum livro encontrado.")

#Remover livro

def remover_livro(livros):
    titulo = input("Título do livro para remover: ").strip().lower()

    for livro in livros:
        if livro["titulo"].lower() == titulo:
            livros.remove(livro)
            salvar_dados(livros)
            print("Livro removido com sucesso.")
            return
        
    print("Livro não encontrado.")

#Menu

def menu():
    livros = carregar_dados()

    while True:
        print("""
=== Biblioteca ===

1 - Adicionar livro
2 - Listar livros
3 - Buscar livro
4 - Remover livro
5 - Sair
""")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_livros(livros)

        elif opcao == "2":
            listar_livros(livros)

        elif opcao == "3":
            buscar_livro(livros)

        elif opcao == "4":
            remover_livro(livros)

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

menu()