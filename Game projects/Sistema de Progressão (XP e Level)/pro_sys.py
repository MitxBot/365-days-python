import math

class Player:
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.xp_to_next = self.calculate_xp()

    def calculate_xp(self):
        return int(100*(self.level **1.5))
    
    def gain_xp(self,amount):
        print(f"\n{self.name} ganhou {amount} XP!")
        self.xp += amount
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"\nLEVEL UP! Agora você é nível {self.level}!")

        #Aumenta atributos

        self.hp += 20
        self.attack += 5
        self.defense += 3

        #Recalcula XP necessário

        self.xp_to_next = self.calculate_xp()

        #Mostra status

        self.show_status()

    def show_status(self):
        print(f"""
Status de {self.name}:
Level: {self.level}
XP: {self.xp}/{self.xp_to_next}
HP: {self.hp}
Ataque: {self.attack}
Defesa: {self.defense}
""")
        
#--- Teste do sistema ---

player = Player("Herói")

player.show_status()

#Simulando batalhas

player.gain_xp(50)
player.gain_xp(80)
player.gain_xp(200)