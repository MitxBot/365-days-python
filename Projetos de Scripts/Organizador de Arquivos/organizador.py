import os
import shutil

#Caminho da pasta onde estão os arquivos

PASTA = r"C:\\Users\\SeuUsuario\\Downloads"

#Palavras-chave e suas respectivas pastas

categorias = {
    "Documentos" : [
        "relatorio",
        "trabalho",
        "contrato",
        "documento",
        "pdf"
    ],

    "Imagens" : [
        "foto",
        "imagem",
        "print",
        "wallpaper"
    ],

    "Videos" : [
        "video",
        "filme",
        "anime",
        "serie"
    ]
}

#Cria as pastas caso não existam

for pasta in categorias.keys():
    os.makedirs(os.path.join(PASTA,pasta),exist_ok=True)

os.makedirs(os.path.join(PASTA,"Outros"),exist_ok=True)

#Percorre todos os arquivos

for arquivo in os.listdir(PASTA):

    caminho = os.path.join(PASTA,arquivo)

    #Ignora pastas

    if not os.path.isfile(caminho):
        continue

    nome = arquivo.lower()

    movido = False

    for pasta,palavras in categorias.items():
        if any(palavras in nome for palavra in palavras):
            destino = os.path.join(PASTA,pasta,arquivo)
            shutil.move(caminho,destino)
            print(f"{arquivo} > {pasta}")
            movido = True
            break

    if not movido:
        destino = os.path.join(PASTA,"Outros",arquivo)
        shutil.move(caminho,destino)
        print(f"{arquivo} > Outros")

print("\nOrganização concluída!")