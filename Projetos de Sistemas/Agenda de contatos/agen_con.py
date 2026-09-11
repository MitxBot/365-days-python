agenda = []

def adicionar_contato():
    print("\n=== Adicionar Contato ===")

    nome = input("Nome: ")
    contato = input("Contato: ")
    email = input("Email: ")

    contato = {
         "nome" : nome,
         "contato" : contato,
         "email" : email
    }

    agenda.append(contato)

    print("Contato adicionado com sucesso!")

def listar_contato():
    print("\n=== Lista de Contatos ===")

    if not agenda:
        print("Nenhum contato cadastrado.")
        return
    
    for i,contato in enumerate(agenda,start=1):
        print(f"\nContato {i}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")

def buscar_contato():
    print("\n=== Buscar Contato ===")

    nome_busca = input("Digite o nome do contato: ")

    encontrado = False

    for contato in agenda:
        if contato["nome"].lower() == nome_busca.lower():
            print("\nContato encontrado:")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            encontrado = True

    if not encontrado:
        print("Contato não encontrado.")

def remover_contato():
    print("\n=== Remover Contato ===")

    nome_remover = input("Digite o nome do contato: ")

    for contato in agenda:
        if contato["nome"].lower() == nome_remover.lower():
            agenda.remove(contato)
            print("Contato removido com sucesso!")
            return
        
    print("Contato não encontrado.")

while True:
    print("\n=== Agenda de Contatos ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()

    elif opcao == "2":
        listar_contato()

    elif opcao == "3":
        buscar_contato()

    elif opcao == "4":
        remover_contato()

    elif opcao == "5":
        print("Encerrando agenda...")
        break

    else:
        print("Opção inválida!")