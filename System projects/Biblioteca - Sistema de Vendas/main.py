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

def listar_livros_menu():

    print("===== Livros =====")

    livros = listar_livros()

    if not livros:
        print("Nenhum livro encontrado.")
        return

    for livro in livros:

        livro_id = livro[0]
        titulo = livro[1]
        autor = livro[2]
        preco = livro[3]
        estoque = livro[4]

        print(
            f"[{livro_id}]"
            f"{titulo} |"
            f"Autor: {autor} |"
            f"R$ {preco:.2f} |"
            f"Estoque: {estoque}"
        )

def cadastrar_cliente_menu():

    print("\n===== Cadastrar Cliente =====")

    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    if not nome:
        print("O nome é obrigatório.")
        return

    try:
        cadastrar_cliente(
            nome,
            email or None
        )

        print("Cliente cadastrado com sucesso!")

    except Exception:
        print("Não foi possível cadastrar o cliente.")

def listar_cliente_menu():

    print("===== Clientes =====")

    clientes = listar_clientes()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:

        cliente_id = cliente[0]
        nome = cliente[1]
        email = cliente[3]

        print(
            f"[{cliente_id}]"
            f"{nome} |"
            f"{email or 'Sem e-mail'}"
        )

def realizar_venda_menu():

    print("\n===== Nova Venda =====")

    listar_livros()

    cliente_input = input(
        "\nID do cliente: "
        "(Enter para venda sem cliente): "
    ).strip()

    cliente_id = (
        int(cliente_input)
        if cliente_input
        else None
    )

    itens = []

    while True:

        livro_input = input(
            "ID do Livro: "
            "(Enter para finalizar): "
        ).strip()