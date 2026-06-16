import sys

#Definição das classes de RPG

classes = {
    "Guerreiro" : 0,
    "Mago" : 0,
    "Arqueiro" : 0,
    "Ladino" : 0,
    "Clérigo" : 0
}

def perguntar(pergunta,opcoes):
    print("\n" + pergunta)
    for i,opcao in enumerate(opcoes,1):
        print(f"{i}. {opcao["texto"]}")
    
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]["pontos"]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Digite apenas números.")

def aplicar_pontos(pontos):
    for classe, valor in pontos.items():
        classes[classe] += valor

def mostrar_resultado():
    print("\nCalculando sua classe...\n")

    for classe, pontos in classes.items():
        print(f"{classe}: {pontos} pontos")
        
    melhor_classe = max(classes,key=classes.get)

    print("\n=================================")
    print(f"Sua classe de RPG é: {melhor_classe}!")
    print("=================================\n")

    descricoes = {
        "Guerreiro" : "Forte e resistente, especialista em combate corpo a corpo.",
        "Mago" : "Domina magia e conhecimento arcano.",
        "Arqueiro" : "Ágil e preciso, ataca à distância.",
        "Ladino" : "Furtivo e estratégico, especialista em ataques rápidos.",
        "Clérigo" : "Curandeiro e protetor, usa poderes divinos."
    }

    print("Descrição:")
    print(descricoes[melhor_classe])

def main():
    print("=== Questionário de Classe RPG ===")

    #Pergunta 1

    p1 = perguntar(
        "Qual dessas qualidades mais te define?",
        [
            {"texto" : "Força física", "pontos" : {"Guerreiro" : 2}},
            {"texto" : "Inteligência", "pontos" : {"Mago" : 2}},
            {"texto" : "Precisão", "pontos" : {"Arqueiro":2}},
            {"texto" : "Astúcia", "pontos" : {"Ladino":2}},
            {"texto" : "Empatia", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p1)

    #Pergunta 2

    p2 = perguntar(
        "Como você prefere resolver problemas?",
        [
            {"texto" : "", "pontos" : {"Guerreiro":2}},
            {"texto" : "", "pontos" : {"Mago":2}},
            {"texto" : "", "pontos" : {"Arqueiro":2}},
            {"texto" : "", "pontos" : {"Ladino":2}},
            {"texto" : "", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p2)

    #Pergunta 3

    p3 = perguntar(
        "Qual arma você escolheria?",
        [
            {"texto" : "Espada", "pontos" : {"Guerreiro":2}},
            {"texto" : "ajado mágico", "pontos" : {"Mago":2}},
            {"texto" : "Arco e flecha", "pontos" : {"Arqueiro":2}},
            {"texto" : "Adagas", "pontos" : {"Ladino":2}},
            {"texto" : "Símbolo sagrado", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p3)

    #Pergunta 4

    p4 = perguntar(
        "Qual ambiente você prefere?",
        [
            {"texto" : "Campo de batalha", "pontos" : {"Guerreiro":2}},
            {"texto" : "Biblioteca antiga", "pontos" : {"Mago":2}},
            {"texto" : "Floresta", "pontos" : {"Arqueiro":2}},
            {"texto" : "Sombras da cidade", "pontos" : {"Ladino":2}},
            {"texto" : "Templo", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p4)

    #Pergunta 5

    p5 = perguntar(
        "Qual papel você teria em um grupo?",
        [
            {"texto" : "Linha de frente", "pontos" : {"Guerreiro":2}},
            {"texto" : "Suporte mágico", "pontos" : {"Mago":2}},
            {"texto" : "Ataque à distância", "pontos" : {"Arqueiro":2}},
            {"texto" : "Infiltração", "pontos" : {"Ladino":2}},
            {"texto" : "Cura e proteção", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p5)

    #Pergunta 6

    p6 = perguntar(
        "O que mais te motiva?",
        [
            {"texto" : "Honra", "pontos" : {"Guerreiro":2}},
            {"texto" : "Conhecimento", "pontos" : {"Mago":2}},
            {"texto" : "Liberdade", "pontos" : {"Arqueiro":2}},
            {"texto" : "Dinheiro", "pontos" : {"Ladino":2}},
            {"texto" : "Fé", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p6)

    #Pergunta 7

    p7 = perguntar(
        "Como você reage ao perigo?",
        [
            {"texto" : "Enfrento de frente", "pontos" : {"Guerreiro":2}},
            {"texto" : "Analiso a situação", "pontos" : {"Mago":2}},
            {"texto" : "Mantenho distância", "pontos" : {"Arqueiro":2}},
            {"texto" : "Evito ser visto", "pontos" : {"Ladino":2}},
            {"texto" : "Protejo os outros", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p7)

    #Pergunta 8

    p8 = perguntar(
        "Qual habilidade você gostaria de ter?",
        [
            {"texto" : "Força sobre-humana", "pontos" : {"Guerreiro":2}},
            {"texto" : "Lançar feitiços", "pontos" : {"Mago":2}},
            {"texto" : "Mira perfeita", "pontos" : {"Arqueiro":2}},
            {"texto" : "Invisibilidade", "pontos" : {"Ladino":2}},
            {"texto" : "Cura divina", "pontos" : {"Clérigo":2}}
        ]
    )
    aplicar_pontos(p8)

    mostrar_resultado()

if __name__ == "__main__":
    main()