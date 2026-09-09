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

def listar_livros():

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

def buscar_livro(livro_id):

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

def listar_clientes():

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

def registrar_venda(cliente_id,itens):

    conexao = conectar()
    cursor = conexao.cursor

    try:
        total = 0
        itens_processados = []

        for item in itens:
            livro_id = item["livro_id"]
            quantidade = item["quantidade"]

            cursor.execute(
                """
                SELECT titulo, preco, estoque
                FROM livros
                WHERE id = ?
                """,
                (livro_id,)
            )

            livro = cursor.fetchone()

            if livro is None:
                raise ValueError(
                    f"Livro com ID {livro_id} não encontrado!"
                )

            titulo = livro[0]
            preco = livro[1]
            estoque = livro[2]

            if quantidade <= 0:
                raise ValueError(
                    "A quantidade deve ser maior que zero."
                )

            if estoque < quantidade:
                raise ValueError(
                    f"Estoque insuficiente para '{titulo}'. "
                    f"Disponível: {estoque}"
                )

            subtotal = preco * quantidade

            total += subtotal

            itens_processados.append(
                (
                    livro_id,
                    quantidade,
                    preco,
                    subtotal
                )
            )

            cursor.execute(
                """
            INSERT INTO vendas (cliente_id, total)
            VALUES (?, ?)
                """,
                (cliente_id,total)
            )

            venda_id = cursor.lastrowid

            for item in itens_processados:
                livro_id = item[0]
                quantidade = item[1]
                preco = item[2]
                subtotal = item[3]

                cursor.execute(
                    """
                    INSERT INTO itens_venda
                (
                    venda_id,
                    livro_id,
                    quantidade,
                    preco_unitario,
                    subtotal
                )
                VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                    venda_id,
                    livro_id,
                    quantidade,
                    preco,
                    subtotal
                    )
                )

                cursor.execute(
                    """
                UPDATE livros
                SET estoque = estoque - ?
                WHERE id = ?
                    """,
                    (
                        quantidade,
                        livro_id
                    )
                )

                conexao.commit()

                return venda_id,total

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()

def listar_vendas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT
            vendas.id,
            clientes.nome,
            vendas.data,
            vendas.total

        FROM vendas

        LEFT JOIN clientes
        ON clientes.id = vendas.cliente_id

        ORDER BY vendas.id DESC
        """
    )

    vendas = cursor.fetchall()

    conexao.close()

    return vendas

def detalhes_venda(venda_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT
            livros.titulo,
            itens_venda.quantidade,
            itens_venda.preco_unitario,
            itens_venda.subtotal

        FROM itens_venda

        JOIN livros
        ON livros.id = itens_venda.livro_id

        WHERE itens_venda.venda_id = ?
        """,
        (venda_id,)
    )

    itens = cursor.fetchall()

    conexao.close()

    return itens