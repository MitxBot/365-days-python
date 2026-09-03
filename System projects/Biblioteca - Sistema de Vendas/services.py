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