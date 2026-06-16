import random

#===== DADOS BASE =====

prefixes = ["Pyro","Aqua","Terra","Volt","Shadow","Lumi","Frost"]
sufixes = ["ling","zor","mon","drake","beast","gon","nix"]

types = ["Fire","Water","Earth","Electric","Dark","Light","Ice"]

abilities = {
    "Fire" : ["Chama Viva","Explosão Flamejante"],
    "Water" : ["Jato d'Água","Maré Alta"],
    "Earth" : ["Impacto Sísmico","Pele de Pedra"],
    "Electric" : ["Choque","Tempestade Elétrica"],
    "Dark" : ["Sombra Mortal","Toque Sombrio"],
    "Light" : ["Raio Sagrado","Cura Divina"],
    "Ice" : ["Congelar","Tempestade de Gelo"]
}

rarities = ["Common","Rare","Epic","Legendary"]

#===== CLASSE =====

class Creature:
    def __init__(self,name,type_,hp,attack,defense,ability,rarity,description):
        self.name = name
        self.type = type_
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.ability = ability
        self.rarity = rarity
        self.description = description

    def show(self):
        print(f"\n Nova Criatura Gerada!")
        print(f"Nome: {self.name}")
        print(f"Tipo: {self.type}")
        print(f"HP: {self.hp} ATK: {self.attack} DEF: {self.defense}")
        print(f"Habilidades: {self.ability}")
        print(f"Raridade: {self.rarity}")
        print(f"Descrição: {self.description}")

#===== GERADOR =====

def generate_name():
    return random.choice(prefixes) + random.choice(sufixes)

def generate_rarity():
    roll = random.random()
    if roll < 0.6:
        return "Common"
    elif roll < 0.85:
        return "Rare"
    elif roll < 0.97:
        return "Epic"
    else:
        return "Legendary"
    
def generate_stats(rarity):
    base = {
        "Common" : 50,
        "Rare" : 70,
        "Epic" : 90,
        "Legendary" : 120
    }[rarity]

    hp = base + random.randint(-10,20)
    attack = base // 2 + random.randint(-5,15)
    defense = base // 2 + random.randint(-5,15)

    return hp,attack,defense

def generate_description(name,type_,rarity):
    return f"{name} é uma criatura do tipo {type_} com poder {rarity.lower()}."

def generate_creature():
    name = generate_name()
    type_ = random.choice(types)
    rarity = generate_rarity()
    hp,attack,defense = generate_stats(rarity)
    ability = random.choice(abilities[type_])
    description = generate_description(name,type_,rarity)

    return Creature(name,type_,hp,attack,defense,ability,rarity,description)

#===== TESTE =====

for _ in range(3):
    c = generate_creature()
    c.show()