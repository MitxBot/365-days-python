import random

#Raridades e probabilidades

raridades = [
    "Comum",
    "Rare",
    "Super Rare",
    "Ultra Rare"
]

probalidades = [
    55,  # Comum
    35,  # Rare
    7.5, # Super Rare
    2.5  # Ultra Rare
]

#Contador de raridades obtidas

inventario = {
    "Comum": 0,
    "Rare": 0,
    "Super Rare": 0,
    "Ultra Rare": 0
}

while True:

    print("\n=== Pack opening ===")
    print("1 - Comprar")
    print("2 - Ver inventário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        resultado = random.choices(
            raridades,
            weights=probalidades,
            k=1
        )[0]

        inventario[resultado] += 1
        print(f"\nVocê obteve: {resultado}!")

    elif opcao == "2":
        print("=== Invetário ===")

        for raridade,quantidade in inventario.items():
            print(f"{raridade}:{quantidade}")

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Erro,Opção inválida!")

"""
Um simulador simples que simula pack opening de Yu-Gi-Oh.
O simulador utiliza o drop rate do Master Duel.
"""