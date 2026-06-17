from pathlib import Path
import shutil

PASTA = Path("Coloque o caminho do arquivo aqui")#Exemplo: C:\\Users\\PC\\Documents\\PDFs

tipos = {
    ".jpg" : "Imagens",
    ".png" : "Imagens",
    ".pdf" : "PDFs",
    ".mp4" :"Videos",
    ".zip" : "Compactados"
}

for arquivo in PASTA.iterdir():

    if arquivo.is_file():

        extensao = arquivo.suffix.lower()

        if extensao in tipos:

            destino = PASTA / tipos[extensao]
            destino.mkdir(exist_ok=True)

            shutil.move(
                str(arquivo),
                str(destino / arquivo.name)
            )

print("Arquivos organizados!")