class classeRPG:
    def __init__(self,nome,hp,ataque,defesa,habilidades):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = habilidades

    def mostrar_classe(self):
        print(f"\nClasse: {self.nome}")
        print(f"HP: {self.hp}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        print(f"Habilidades: ")
        for h in self.habilidades:
            print(f" - {h}")

class Player:
    def __init__(self,nome,classe):
        self.nome = nome
        self.classe = classe

        #Atributos da classe

        self.hp = classe.hp
        self.ataque = classe.ataque
        self.defesa = classe.defesa
        self.habilidades = classe.habilidades.copy()

    def mostrar_status(self):
        print(f"\n {self.nome} {self.classe.nome}")
        print(f"Hp: {self.hp}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        print(f"Habilidades: ")
        for h in self.habilidades:
            print(f" - {h}")

def criar_classe():
        
        def pedir_numero(mensagem):
            while True:
                try:
                    valor = int(input(mensagem))
    
                    if valor <= 0:
                        print("O valor deve ser maior que 0!")
                        continue    
        
                    return valor
                
                except ValueError:
                    print("Digite apenas números!")
        
        print("=== Criador de Classe ===")

        nome = input("Nome da classe: ")

        hp = pedir_numero("HP base: ")
        ataque = pedir_numero("Ataque base: ")
        defesa = pedir_numero("Defesa base: ")

        habilidades = []
        
        while True:
            h = input("Adicionar habilidade (ou 'sair'): ").strip()
            if h.lower() == "sair":
                break
            if h == "":
                print("Digite uma habilidade válida!")
                continue

            habilidades.append(h)
        
        return classeRPG(nome,hp,ataque,defesa,habilidades)
    
#--- USO DO SISTEMA ---

#Criar classe personalizada

classe_custom = criar_classe()
classe_custom.mostrar_classe()

#Criar jogador com essa classe

nome_player = input("\nNome do jogador: ")
player = Player(nome_player,classe_custom)

#Mostrar status final

player.mostrar_status()