import os
import hashlib

# Configurações

#Caminho da pasta que será analisada

PASTA = r""

#Algoritmo de hash

HASH = "sha256"

#Tamanho do bloco de leitura (1MB)

BUFFER = 1024 * 1024

#Funções

def calcular_hash(arquivo):
    """Calcula o hash de um arquivo."""

    h = hashlib.new(HASH)

    with open(arquivo, "rb") as f:
        
        while True:
            bloco = f.read(BUFFER)
            
            if not bloco:
                break
            
            h.update(bloco)

    return h.hexdigest()

def encontrar_duplicados(pasta):
    """Encontra arquivos duplicados."""

    hashes = {}
    duplicados = []

    for raiz, _, arquivos in os.walk(pasta):

        for nome in arquivos:
            caminho = os.path.join(raiz,nome)

            try:
                hash_arquivo = calcular_hash(caminho)
                if hash_arquivo in hashes:
                    duplicados.append(caminho,hashes[hash_arquivo])
                else:
                    hashes[hash_arquivo] = caminho
            except Exception as erro:
                print(f"Erro ao ler {caminho} : {erro}")
                
    return duplicados

def remover_duplicados(lista):
    """Remove arquivos duplicados."""

    if not lista:
        print("\nNenhum arquivo duplicado encontrado.")
        return
    
    print("\nArquivos duplicados encontrados: ")

    for duplicado, original in lista:
        print("Origal: ", original)
        print("Duplicado: ", duplicado)
        print("-" * 60)

    resposta = input("\nDeseja remover TODOS os duplicados? (s/n):").lower()

    if resposta != "s":
        print("Operação cancelada.")
        return
    
    removidos = 0

    for duplicado, _ in lista:
        try:
            os.remove(duplicado)
            removidos += 1
            print(f"Removido: {duplicado}")

        except Exception as erro:
            print(f"Erro ao remover {duplicado}: {erro}")

    print(f"\nTotal removido: {removidos}")

#Programa

print("Procurando arquivos duplicados...\n")

duplicados = encontrar_duplicados(PASTA)

print("\nFim.")