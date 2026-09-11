from pathlib import Path
import shutil
import time

#Pasta que será organizada

PASTA_DOWNLOADS = Path.home() / "Downloads"

#Tipos de arquivos

TIPOS = {
    "Imagens" : [".png",".jpg","jpeg","gif","webp"],
    "Vídeos" : [".mp4",".mkv",".avi",".mov"],
    "Músicas" : [".mp3",".wav",".flac"],
    "Documentos" : [".pdf",".docx",".txt",".xlsx",".pptx"],
    "Compactados" : [".zip",".rar",".7z"],
    "Programas" : [".exe","msi"],
}

def criar_pasta():
    for pasta in TIPOS.keys():
        caminho = PASTA_DOWNLOADS / pasta
        caminho.mkdir(exist_ok=True)

def mover_arquivo(arquivo):
    extensao = arquivo.suffix.lower()

    for pasta,extensoes in TIPOS.items():
        destino = PASTA_DOWNLOADS / pasta / arquivo.name

        #Evita erro caso o arquivo já exista

        contador = 1
        while destino.exists():
            novo_nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
            destino = PASTA_DOWNLOADS / pasta / novo_nome

        shutil.move(str(arquivo),str(destino))
        print(f"{arquivo.name} -> {pasta}")
        return
    
def organizar():
    print("Organizando arquivos...\n")

    for arquivo in PASTA_DOWNLOADS.iterdir():
        if arquivo.is_file():
            mover_arquivo(arquivo)

    print("\nOrganização concluída!")

#Executa automaticamente a cada 30 segundos

if __name__ == "__main__":
    criar_pasta()

while True:
    organizar()
    time.sleep(30)