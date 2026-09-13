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