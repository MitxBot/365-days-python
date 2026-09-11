num1 = float(input("Digite um número: "))
operacao = input("Digite a operação (+, -, *, /) :")
num2 = float(input("Digite um outro número: "))

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")

else:
    print("Operação inválida!")

print("Resultado: ", resultado)