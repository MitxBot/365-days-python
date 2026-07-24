from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from datetime import datetime
import time

#Pasta que será monitorada
PASTA = Path("monitarada")

#Cria a pasta caso ela não exista
PASTA.mkdir(exist_ok=True)

class Monitor(FileSystemEventHandler):

    def registrar(self,evento,caminho):
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        mensagem = f"[{horario}] {evento}: {caminho}"

        print(mensagem)

        with open("log.txt","a",encoding="utf-8") as arquivo:
            arquivo.write(mensagem + "\n")

    def on_created(self,event):
        if not event.is_directory:
            self.registrar("Arquivo criado",event.src_path)

    def on_deleted(self,event):
        if not event.is_directory:
            self.registrar("Arquivo removido",event.src_path)

    def on_modified(self,event):
        if not event.is_directory:
            self.registrar("Arquivo modificado",event.src_path)

    def on_move(self,event):
        if not event.is_directory:
            self.registrar(
                "Arquivo renomeado",
                f"{event.src_path} > {event.des_path}"
            )

observer = Observer()
observer.schedule(Monitor(),str(PASTA),recursive=True)
observer.start()

print(f"Monitorando a pasta" '{PASTA.resolve()}')
print("Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()