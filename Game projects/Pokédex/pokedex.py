import sqlite3

#Conecta(ou cria)o banco de dados

conexao = sqlite3.connect("pokedex.db")
cursor = conexao.cursor()

#Cria a tabela caso ela não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS pokedex (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo1 TEXT NOT NULL,
    tipo2 TEXT,
    hp INTEGER,
    ataque INTEGER,
    defesa INTEGER
)
""")

conexao.commit()

#Funções

def adicionar_pokemon():
    print("\n=== Novo Pokémon ===")

    nome = input("Nome: ").title()
    tipo1 = input("Tipo 1: ").title()
    tipo2 = input("Tipo 2(Enter se não possuir): ").title()

    hp = input("HP: ")
    ataque = int(input("Ataque: "))
    defesa = int(input("Defesa: "))

    cursor.execute("""
    INSERT INTO pokedex
    (nome,tipo1,tipo2,hp,ataque,defesa)
    VALUES (?, ?, ?, ?, ?, ?)
    """,(nome,tipo1,tipo2,hp,ataque,defesa))

    conexao.commit()

    print("Pokémon cadastrado com sucesso!")

def listar_pokemon():
    print("\n=== Pokédex ===")

    cursor.execute("SELECT * FROM pokedex")
    pokemons = cursor.fetchall()

    if len(pokemons) == 0:
        print("Nenhum Pokémon cadastrado.")
        return

    for pokemon in pokemons:
        print("-" * 40)
        print(f"ID: {pokemon[0]}")
        print(f"Nome: {pokemon[1]}")
        print(f"Tipo 1: {pokemon[2]}")
        print(f"Tipo 2: {pokemon[3]}")
        print(f"HP: {pokemon[4]}")
        print(f"Ataque: {pokemon[5]}")
        print(f"Defesa: {pokemon[6]}")

def procurar_pokemon():
    nome = input("\nNome do Pokémon: ").title()

    cursor.execute(
        "SELECT * FROM pokedex WHERE nome = ?",
        (nome,)
    )

    pokemon = cursor.fetchone()