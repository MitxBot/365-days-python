from pathlib import Path
from zipfile import ZipFile
from datetime import datetime

#Pasta que será copiada

PASTA_ORIGEM = Path(r"")

#Pasta onde os backups serão salvos

PASTA_BACKUP = Path(r"")

PASTA_BACKUP.mkdir(exist_ok=True)

data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

arquivo_backup = PASTA_BACKUP / f"bakcup_{data}.zip"

with ZipFile(arquivo_backup,"w") as zipf:

    for arquivo in PASTA_ORIGEM.rglob("*"):
        if arquivo.is_file():

            zipf.write(
                arquivo,
                arquivo.relative_to(PASTA_ORIGEM)
            )

print(f"Backup criado: ")
print(arquivo_backup)