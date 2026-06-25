import random

palavras = [
    "python",
    "computador",
    "programacao",
    "biblioteca",
    "algoritmo",
    "desenvolvedor",
    "terminal",
    "sistema",
    "automacao",
    "variavel"
]

palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)

letras_tentadas = []

tentativas = 6

print("==== Jogo da Forca ====")

while tentativas > 0:
    print("\nPalavra:","".join(letras_descobertas))
    print("Tentativas restantes:",tentativas)
    print("Letras usadas:",", ".join(letras_tentadas))

    letra = input("\nDigite uma letra: ").lower()

    if len(letra) != 1:
        print("Digite apenas uma letra.")
        continue

    letras_tentadas.append(letra)

    if letra in palavra:

        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra

        print("Acertou!")

    else:
        tentativas -= 1
        print("Errou!")

    if "_" not in letras_descobertas:

        print("\nParabéns!")
        print("Você descobriu a palavra:",palavra)

        break

else:

    print("\nFim de jogo!")
    print("A palavra era:",palavra)