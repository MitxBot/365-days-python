usuarios = {}

def cadastrar():
    print(f"\n=== CADASTRO ===")
    
    usuario = input("Digite um nome de usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    senha = input("Digite uma senha: ")

    usuarios[usuario] = senha

    print("Cadastro realizado com sucesso!")

def login():
    print(f"\n=== LOGIN ===")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"Bem-vindo,{usuario}!")
    else:
        print(f"Usuário ou senha incorretos!")

def listar_usuarios():
    print(f"\n=== USUÁRIOS CADASTRADOS ===")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for usuario in usuarios:
        print(usuario)

while True:
    print(f"\n===== SISTEMA =====")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        login()

    elif opcao == "3":
        listar_usuarios()

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")