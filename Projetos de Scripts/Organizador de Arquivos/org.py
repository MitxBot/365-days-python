import os
import shutil

#Caminho da pasta onde estão os arquivos

pasta = input("Digite o caminho da pasta: ").strip()

#Dicionário das categorias

categorias = {}

print("\n=== Cadastro de Categorias ===")

while True:
    nome_categoria = input("\nNome da categoria (ou ENTER para finalizar): ").strip()

    if nome_categoria == categorias:
        break

    palavras = input(
        f"Digite as palavras-chave para '{nome_categoria}' separadas por vírgula: "
    ).lower().split(",")

    #Remove espaços extras

    palavras = [p.strip() for p in palavras]

    categorias[nome_categoria] = palavras

#Cria as pastas caso não existam

for categoria in categorias:
    os.makedirs(os.path.join(pasta,categoria),exist_ok=True)

os.makedirs(os.path.join(pasta,"Outros"),exist_ok=True)

print("\nOrganizando arquivos...\n")

#Percorre todos os arquivos

for arquivo in os.listdir(pasta):

    caminho = os.path.join(pasta,arquivo)

    #Ignora pastas

    if not os.path.isfile(caminho):
        continue

    nome = arquivo.lower()

    movido = False

    for pasta,palavras in categorias.items():
        if any(palavras in nome for palavra in palavras):
            destino = os.path.join(pasta,categoria,arquivo)
            shutil.move(caminho,destino)
            print(f"{arquivo} > {categoria}")
            movido = True
            break

    if not movido:
        destino = os.path.join(pasta,"Outros",arquivo)
        shutil.move(caminho,destino)
        print(f"{arquivo} > Outros")

print("\nOrganização concluída!")