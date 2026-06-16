import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"

class Tarefa:
    def __init__(self,titulo,descricao,prioridade,concluida=False,criada_em=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida
        self.crida_em - criada_em if criada_em else datetime.now().strtime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return{
            "titulo" : self.titulo,
            "descricao" : self.descricao,
            "prioridade" : self.prioridade,
            "concluida" : self.concluida,
            "criada_em" : self.criada_em
        }
    
    @staticmethod
    def from_dict(data):
        return Tarefa(
            data["titulo"],
            data["descricao"],
            data["prioridade"],
            data["concluida"],
            data["criada_em"]
        )
    
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar()

    def adicionar(self,tarefa):
        self.tarefas.append(tarefa)
        self.salvar()

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for i,tarefa in enumerate(self.tarefas):
            status = "✔" if self.tarefa.concluida else "✘"
            print(f"{i}-{tarefa.titulo} [{status}](Prioridade:{tarefa.prioridade})")

    def detalhar(self,indice):
        try:
            t = self.tarefas[indice]
            print("\n--- DETALHES ---")
            print(f"Título:{t.titulo}")
            print(f"Descrição:{t.descricao}")
            print(f"Prioridade:{t.prioridade}")
            print(f"Concluída:{t.concluida}")
            print(f"Crida em:{t.criada_em}\n")
        except IndexError:
            print("Índice inválido.")

    def concluir(self,indice):
        try:
            self.tarefas[indice].concluida = True
            self.salvar()
        except IndexError:
            print("Índice inválido.")

    def remover(self,indice):
        try:
            del self.tarefas[indice]
            self.salvar()
        except IndexError:
            print("Índice inválido.")

    def salvar(self):
        with open(ARQUIVO,"w") as f:
            json.dump([t.to_dict()for t in self.tarefas],f,indent=4)
        
    def carregar(self):
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO,"r") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa.from_dict(d)for d in dados]

def menu():
        print("""
==== GERENCIADOR DE TAREFAS ====
1. Adicionar tarefa
2. Listar tarefas
3. Ver detalhes
4. Concluir tarefa
5. Remover tarefa
6. Sair
""")
    
def main():
    gerenciador = GerenciadorTarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            titulo = input("Titulo:")
            descricao = input("Descrição:")
            prioridade = input("Prioridade (baixa/média/alta):")
            tarefa = Tarefa(titulo,descricao,prioridade)
            gerenciador.adicionar(tarefa)
            prioridade("Tarefa adicionada!\n")

        elif opcao == "2":
            gerenciador.listar()

        elif opcao == "3":
            indice = int(input("Índice da tarefa:"))
            gerenciador.detalhar(indice)

        elif opcao == "4":
            indice = int(input("Índice da tarefa:"))
            gerenciador.concluir(indice)
            print("Tarefa concluída!\n")

        elif opcao == "5":
            indice = int(input("Índice da tarefa:"))
            gerenciador.remover(indice)
            print("Tarefa removida!\n")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()