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

def remover_tarefa():

    listar_tarefa()

    if not tarefas:
        return

    try:
        numero = int(input("\nDigite o número da tarefa."))

        if 1 <= numero <= len(tarefas):
            tarefa = tarefas.pop(numero - 1)
            print(f"Tarefa '{tarefa['nome']}' removida!")

        else:
            print("Número inválido!")

    except ValueError:
        print("Digite um número válido.")

def menu():

    while True:
        print("\n===== Lista de Tarefas =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("\nDigite uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefa()

        elif opcao == "3":
            concluir_tarefa()

        elif opcao == "4":
            remover_tarefa()

        elif opcao == "5":
            print("Encerrando o programa...")
            break

        else:
            print("Erro,opção inválida!")

menu()