import sqlite3

#Conectar ao banco (ou criar se não existir)

conn = sqlite3.connect("personagens.db")
cursor = conn.cursor()

#Criar tabela

cursor.execute("""
CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    tipo TEXT,
    atributo TEXT,
    sexo TEXT
)
 """)

def criar_personagem():
    print("\n=== Criar novo personagem ===")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    atributo = input("Atributo: ")
    sexo = input("Sexo: ")

    cursor.execute("""
    INSERT INTO personagens(nome,tipo,atributo,sexo)
    values (?,?,?,?)
    """,(nome,tipo,atributo,sexo))

def listar_personagens():
    print("\n=== Lista de personagens ===")

    cursor.execute("SELECT * FROM personagens")
    personagens = cursor.fetchall()

    if not personagens:
        print("Nenhum personagem cadastrado.")
        return
    
    for p in personagens:
        print("""
ID: {p[0]}
Nome: {p[1]}
Tipo: {p[2]}
Atributo: {p[3]}
Sexo: {p[4]}
-------------------------
""")

def menu():
    while True:
        print("""
1 - Criar personagem
2 - Listar personagens
3 - Sair
""")
        escolha = input("Escolha: ")

        if escolha == "1":
            criar_personagem()
        elif escolha == "2":
            listar_personagens()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")

menu()

conn.close()