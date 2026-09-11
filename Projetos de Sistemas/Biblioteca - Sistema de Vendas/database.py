import sqlite3

DATABASE = "biblioteca.db"

def conectar():

    return sqlite3.connect(DATABASE)

def inicializar_banco():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT NOT NULL,

            autor TEXT NOT NULL,

            preco REAL NOT NULL,

            estoque INTEGER NOT NULL
        )
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT NOT NULL,

            email TEXT UNIQUE
        )
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            cliente_id INTEGER,

            data TEXT NOT NULL
                DEFAULT CURRENT_TIMESTAMP,

            total REAL NOT NULL,

            FOREIGN KEY (cliente_id)
                REFERENCES clientes(id)
        )
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_venda (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            venda_id INTEGER NOT NULL,

            livro_id INTEGER NOT NULL,

            quantidade INTEGER NOT NULL,

            preco_unitario REAL NOT NULL,

            subtotal REAL NOT NULL,

            FOREIGN KEY (venda_id)
                REFERENCES vendas(id),

            FOREIGN KEY (livro_id)
                REFERENCES livros(id)
        )
""")

    conexao.commit()
    conexao.close()