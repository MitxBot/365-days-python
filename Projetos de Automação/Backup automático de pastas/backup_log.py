from pathlib import Path
from datetime import datetime

def registrar_log(mensagem):
    log = Path("backup_log.txt")

    with open(log,"a",encoding="utf-8") as arquivo:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        arquivo.write(f"[{data}] {mensagem}\n")