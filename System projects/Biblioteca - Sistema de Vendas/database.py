import sqlite3

DATABASE = "biblioteca.db"

def conectar():

    return sqlite3.connect(DATABASE)