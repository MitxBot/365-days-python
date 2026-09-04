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