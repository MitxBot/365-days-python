#Mini RPG em Python com SQLite
#Tema: Bestiário + Combate simples

import sqlite3
import random

# =========================
# BANCO DE DADOS
# =========================

conn = sqlite3.connect("rpg.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS monstros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    hp INTEGER,
    ataque INTEGER
)
""")

conn.commit()

# =========================
# INSERIR MONSTROS
# =========================

def adicionar_monstro(nome,hp,ataque):
    cursor.execute(
    "INSERT INTO monstros (nome,hp,ataque) VALUES (?,?,?)",
    (nome,hp,ataque)
    )
    conn.commit()

#Adiciona monstros iniciais (se estiver vazio)

cursor.execute("SELECT COUNT (*) FROM monstros")
if cursor.fetchone()[0] == 0:
    adicionar_monstro("Slime",10,2)
    adicionar_monstro("Goblin",20,5)
    adicionar_monstro("Dragão",100,20)

# =========================
# LISTAR MONSTROS
# =========================

def listar_monstros():
    cursor.execute("SELECT (*) FROM monstros")
    return cursor.fetchall()

# =========================
# SISTEMA DE COMBATE
# =========================

def batalhar():
    monstro = listar_monstros()
    monstro = random.choice(monstro)

    nome,hp,ataque = monstro[1],monstro[2],monstro[3]
    jogador_hp = 50

    print(f"\n Você encontrou um {nome}!")

    while hp > 0 and jogador_hp > 0:
        acao = input("\n1 - Atacar\n2 - Fugir\n - Escolha: ")
    
        if acao == "1":
            dano = random.randint(5,10)
            hp -= dano
            print(f"Você causou {dano} de dano!")

            if hp > 0:
                jogador_hp -= ataque
                print(f"O {nome} atacou e causou {ataque} de dano!")

        elif acao == "2":
            print("Você fugiu!")
            return
    
    if jogador_hp > 0:
        print(f"\n Você derrotou o {nome}!")

    else:
        print(f"\n Você foi derrotado...")

# =========================
# MENU PRINCIPAL
# =========================

def menu():
    while True:
        print("""
==== MINI RPG ====
1 - Ver monstros
2 - Batalhar
3 - Adicionar monstro
4 - Sair
""")
        opcao = input("Escolha: ")

        if opcao == "1":
            monstro = listar_monstros()
            for m in monstro:
                print(f"ID: {m[0]} / Nome: {m[1]} / HP: {m[2]} / ATK: {m[3]}")

        elif opcao == "2":
            batalhar()
        
        elif opcao == "3":
            nome = input("Nome: ")
            hp = int(input("HP: "))
            atk = int(input("Ataque: "))
            adicionar_monstro(nome,hp,atk)
            print("Monstro adicionado!")
        
        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

# =========================
# EXECUTAR
# =========================

if __name__ == "__main__":
    menu()
    conn.close()