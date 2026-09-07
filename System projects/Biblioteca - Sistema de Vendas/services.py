from database import conectar

def cadastrar_livro(titulo,autor,preco,estoque):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO livros (titulo, autor, preco, estoque)
        VALUES (?, ?, ?, ?)
        """,
        (titulo, autor, preco, estoque)
    )

    conexao.commit()
    conexao.close()

def listar_livro():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, titulo, autor, preco, estoque
        FROM livros
        ORDER BY titulo
        """
    )

    livros = cursor.fetchall()

    conexao.close()

    return livros

def buscar_livros(livro_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, titulo, autor, preco, estoque
        FROM livros
        WHERE id = ?
        """,
        (livro_id,)
    )

    livro = cursor.fetchone()

    conexao.close()

    return livro

def cadastrar_cliente(nome,email):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
        """,
        (nome,email)
    )

    conexao.commit()
    conexao.close()

def listar_cliente():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, nome, email
        FROM clientes
        ORDER BY nome

        """
    )

    clientes = cursor.fetchall()

    conexao.close()

    return clientes