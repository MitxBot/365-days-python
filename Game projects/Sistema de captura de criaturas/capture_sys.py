import random

class Creature:
    def __init__(self,name,max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
    
    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 1:
            self.hp = 1 #Não deixa morrer (estilo Pokémon)
    
#tipos de bolas

balls = {
    "normal" : 1.0,
    "great" : 1.5,
    "ultra" : 2.0
}

def calculate_capture_chance(creature,ball_type):
    hp_factor = (creature.max_hp - creature.hp) / creature.max_hp
    ball_bonus = balls.get(ball_type,1)

    chance = hp_factor *0.7 + .01 #base mínima
    chance *= ball_bonus

    return min(chance,0.95) #limite de 95%

def try_capture(creature,ball_type):
    chance = calculate_capture_chance(creature,ball_type)
    roll = random.random()

    print(f"\n Tentando capturar{creature.name}...")
    print(f"Chance: {round(chance * 100,1)}%")

    if roll <chance:
        print("Captura bem-sucedida!")
        return True
    
    else:
        print("A criatura escapou!")
        return False

#===== TESTE =====

wild = Creature("Aquabub",50)

#simula batalha

wild.take_damage(30)

print(f"{wild.name} HP: {wild.hp}/{wild.max_hp}")

captured = try_capture(wild,"great")

if captured:
    print(f"{wild.name} foi adicionado à sua Pokédex!")