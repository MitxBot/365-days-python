import random

#Lista com os adjetivos usados para o nickname.

adjetivos = [
    "Dark", "Swift", "Silent", "Shadow", "Crazy",
    "Lucky", "Epic", "Nova", "Frost", "Iron",
    "Blue", "Ghost", "Rapid", "Cyber", "Alpha"
]

#Lista com os substantivos usados para o nickname.

substantivos = [
    "Wolf", "Tiger", "Falcon", "Dragon", "Phoenix",
    "Hunter", "Knight", "Wizard", "Storm", "Raven",
    "Lion", "Snake", "Bear", "Eagle", "Fox"
]

def gerar_usuario():
    adjetivo = random.choice(adjetivos)
    substantivo = random.choice(substantivos)
    numero = random.randint(100,9999)#Define o alcance dos números que vira depois do nickname.Por exemplo:ShadowLion8418

    return f"{adjetivo}{substantivo}{numero}"

while True:
    print("\n=== Gerador de Usuário ===")
    print("1 - Gerar usuário")
    print("2 - Gerar 5 usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nUsuário gerado: ")
        print(gerar_usuario())

    elif opcao == "2":
        print("\nUsuários gerados: ")
        for i in range(5):
            print(f"{i + 1}. {gerar_usuario()}")

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida!")