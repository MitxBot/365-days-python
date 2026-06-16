import random

largura = 10
altura = 10

mapa = []

for y in range(altura):
    linha = []
    for x in range(largura):
        terreno = random.choice(["Floresta","Praia","Pico","Planice"])
        linha.append(terreno)
    mapa.append(linha)

for linha in mapa:
    print("".join(linha))