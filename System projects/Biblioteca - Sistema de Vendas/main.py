from database import inicializar_banco
from services import (
    cadastrar_livro,
    listar_livros,
    cadastrar_cliente,
    listar_clientes,
    buscar_livro,
    registrar_venda,
    listar_vendas,
    detalhes_venda
)

def ler_float(mensagem):

    while True:
        try:
            valor = float(input(mensagem).replace(",","."))

            if valor < 0:
                raise ValueError

            return valor

        except ValueError:
            print("Digite um número válido.")

def ler_int(mensagem,minimo=None):

    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                raise ValueError

            return valor

        except ValueError:
            print("Digite um número inteiro válido.")

def cadastrar_livro_menu():

    print("\n===== Cadastrar Livro =====")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    preco = ler_float("Preço R$: ")
    estoque = ler_int("Quantidade em estoque: ",0)

    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return

    cadastrar_livro(
        titulo,
        autor,
        preco,
        estoque
    )

    print("Livro cadastrado com sucesso!")