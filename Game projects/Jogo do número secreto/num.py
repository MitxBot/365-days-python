import random

def jogo_numero_secreto():
    numero_secreto = random.randint(1, 100)  #Número secreto entre 1 e 100
    tentativas = 0

    print("Bem-vindo ao jogo de Número Secreto!")
    print("Tente adivinhar o número secreto (entre 1 e 100).")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativa(s).")
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

#Inicia o jogo
jogo_numero_secreto()