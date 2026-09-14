tarefas = []

def adicionar_tarefa():

    tarefa = input("Digite uma tarefa: ").strip()

    if tarefa:
        tarefas.append({
            "nome" : tarefa,
            "concluida" : False
        })

        print("Tarefa adicionada!")

    else:
        print("A tarefa não pode estar vazia.")

def listar_tarefa():

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("===== Tarefas =====")

    for i,tarefa in enumerate(tarefas,start=1):
        status = "Completo" if tarefa["concluida"] else ""

        print(f"{i}. [{status}] {tarefa['nome']}")

def concluir_tarefa():

    listar_tarefa()

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa."))

        if 1 <= numero <= len(tarefas):
            tarefas[numero-1]["concluida"]=True
            print("Tarefa concluída!")

        else:
            print("Número inválido!")

    except ValueError:
        print("Digite um número válido.")