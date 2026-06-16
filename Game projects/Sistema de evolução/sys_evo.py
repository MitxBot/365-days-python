import random

class Creature:
    def __init__(self,name,level = 1,friendship = 0):
        self.name = name
        self.level = level
        self.friendship = friendship
        self.item = None

    def gain_level(self):
        self.level += 1
        self.friendship += random.randint(1,5)
        print(f"{self.name} Subiu para o nível {self.level}!")
        print(f"A amizade atual é {self.friendship}")
    
    def give_item(self,item):
        self.item = item
        print(f"{self.name} recebeu: {item}!")

#Sistema de evolução

evolutions = {
    "Flameling" : {
        "evolves_to" : "Flareonix",
        "level": 5
    },
    "Aquabub" : {
        "evolves_to" : "Aquarion",
        "item" : "Water Stone"
    },
    "Leafy" : {
        "evolves_to" : "Florania",
        "friendship" : 15

    }
}

def check_evolution(creature):
    if creature.name not in evolutions:
        return creature
    
    evo = evolutions[creature.name]

#Verificar nível

    if "level" in evo and creature.level >= evo["level"]:
        return evolve(creature,evo["evolves_to"])

#Verificar item

    if "item" in evo and creature.item == evo["item"]:
        return evolve(creature,evo["evolves_to"])

#Verificar amizade

    if "friendship" in evo and creature.friendship >= evo["friendship"]:
        return evolve(creature,evo["evolves_to"])

    return creature

def evolve(creature,new_name):
    print(f"\n {creature.name} está evoluindo...")
    print(f"{creature.name} evoliu para {new_name} !\n")
    creature.name = new_name
    return creature

#===== TESTE =====

creature = Creature("Flameling")

for _ in range(6):
    creature.gain_level()
    creature = check_evolution(creature)

#Teste com item

creature2 = Creature("Aquabub")
creature2.give_item("Water Stone")
creature2 = check_evolution(creature2)

#Teste com amizade

creature3 = Creature("Leafy")
for _ in range(5):
    creature3.gain_level()
    creature3 = check_evolution(creature3)