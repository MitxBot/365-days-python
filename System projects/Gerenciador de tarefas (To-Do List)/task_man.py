tarefas = []

def adicionar_tarefa():
    print("\n=== ADICIONAR TAREFA ===")

    titulo = input("Digite a tarefa: ")

    tarefa = {
        "titulo" : titulo,
        "concluida" : False
    }

    tarefas.append(tarefa)

    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\n=== LISTA DE TAREFAS ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for i,tarefa in enumerate(tarefas,start=1):

        status = "O" if tarefa["concluida"] else "X"

        print(f"{i}. [{status}] {tarefa['titulo']}")

def concluir_tarefa():
    print("\n=== CONCLUIR TAREFA ===")

    listar_tarefas()

    if not tarefas:
        return
    
    try:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa concluída!")
        
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite apenas números")

def remover_tarefa():
    print("\n=== REMOVER TAREFA ===")

    listar_tarefas()

    if not tarefas:
        return
    
    try:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print(f"Tarefa '{removida['titulo']}'removida")

        else:
            print("Número inválido.")

    except ValueError:
        print("Digite apenas números.")

while True:
    print("\n===== TO-DO LIST =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")