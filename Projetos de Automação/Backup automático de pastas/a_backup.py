from pathlib import Path
from zipfile import ZipFile
from datetime import datetime

#Pasta que será copiada
PASTA_ORIGEM = Path(r"")

#Pasta onde os backups serão salvos
PASTA_BACKUP = Path(r"")

#Cria a pasta de backup caso ela ainda não exista e evita erro caso a pasta já exista
PASTA_BACKUP.mkdir(exist_ok=True)

#Obtém a data e a hora atuais no formato Ano-Mês-Dia_Hora-Minuto-Segundo
nome = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#Define o nome e o caminho do arquivo .zip
arquivo_zip = PASTA_BACKUP / f"bakcup_{nome}.zip"

with ZipFile(arquivo_zip,"w") as zipf:

    for arquivo in PASTA_ORIGEM.rglob("*"):
        if arquivo.is_file():

            zipf.write(
                arquivo,
                arquivo.relative_to(PASTA_ORIGEM)
            )

#Procura todos os backups existentes na pasta de backup
backups = sorted(
    PASTA_BACKUP.glob("backup_*.zip"),
    key=lambda x: x.stat().st_mtime
)

#Mantém até 5 backups
while len(backups) > 5:
    backups[0].unlink()
    backups.pop(0)

print("Backup concluído com sucesso!")