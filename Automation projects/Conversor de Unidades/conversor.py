FATOR_CONVERSAO = 1.60934

def km_para_milhas(km):
    return km / FATOR_CONVERSAO

def milhas_para_km(milhas):
    return milhas * FATOR_CONVERSAO

while True:
    print("\n=== Conversor de Unidades ===")
    print("1 - Quilômetros > Milhas")
    print("2 - Milhas > Quilômetros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            km = float(input("Digite a distância em quilômetros: "))
            milhas = km_para_milhas(km)
            print(f"\n{km:.2f} km = {milhas:.2f} milhas")

        except ValueError:
            print("Digite um número válido!")

    elif opcao == "2":
        try:
            milhas = float(input("Digite a distância em milhas: "))
            km = milhas_para_km(milhas)
            print(f"\n{milhas:.2f} milhas = {km:.2f} km")

        except ValueError:
            print("Digite um número válido!")

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida!")