from pathlib import Path
from zipfile import ZipFile
from datetime import datetime

#Pasta que será copiada

PASTA_ORIGEM = Path(r"")

#Pasta onde os backups serão salvos

PASTA_BACKUP = Path(r"")

PASTA_BACKUP.mkdir(exist_ok=True)

nome = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

arquivo_zip = PASTA_BACKUP / f"bakcup_{nome}.zip"

with ZipFile(arquivo_zip,"w") as zipf:

    for arquivo in PASTA_ORIGEM.rglob("*"):
        if arquivo.is_file():

            zipf.write(
                arquivo,
                arquivo.relative_to(PASTA_ORIGEM)
            )

backups = sorted(
    PASTA_BACKUP.glob("backup_*.zip"),
    key=lambda x: x.stat().st_mtime
)

while len(backups) > 5:
    backups[0].unlink()
    backups.pop(0)

print("Backup concluído")