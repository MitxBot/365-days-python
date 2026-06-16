import random

class Attack:
    def __init__(self,name,power):
        self.name = name
        self.power = power

class Creature:
    def __init__(self,name,type_,hp,attack,defense,attacks):
        self.name = name
        self.type = type_
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.attacks = attacks
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self,damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def choose_attack(self,):
        return random.choice(self.attacks)

#Sistema de dano

def calculate_damage(attacker,defender,attack):
        base = attacker.attack + attack.power
        damage = base - defender.defense
        
    #Mínimo de dano
        damage = max(1,damage)
    #Crítico
        if random.random() <0.2:
            print("Ataque crítico!")
            damage *= 2
        return damage

#Loop de batalha

def battle(creature1,creature2):
        turn = 1

        print(f"\n Batalha: {creature1.name} Vs. {creature2.name} \n")

        while creature1.is_alive() and creature2.is_alive():
            print(f"\n Turno {turn} ")
        
            #Criatura 1 ataca

            attack1 = creature1.choose_attack()
            damage1 = calculate_damage(creature1,creature2,attack1)
            creature2.take_damage(damage1)

            print(f"{creature1.name} usou {attack1.name}!")
            print(f"Causou {damage1} de dano")
            print(f"{creature2.name} HP: {creature2.hp}/{creature2.max_hp}")

            if not creature2.is_alive():
                print(f"\n {creature1.name} venceu!")
                break

            #Criatura 2 ataca

            attack2 = creature2.choose_attack()
            damage2 = calculate_damage(creature2,creature1,attack2)
            creature1.take_damage(damage2)

            print(f"{creature2.name} usou {attack2.name}!")
            print(f"Causou {damage2} de dano")
            print(f"{creature1.name} HP: {creature1.hp}/{creature2.max_hp}")

            if not creature1.is_alive():
                print(f"\n {creature2.name} venceu!")
                break

            turn += 1

#===== TESTE =====

#Ataques

fireball = Attack("Fireball",8)
scratch = Attack("Scratch",5)
water_blast = Attack("Water Blast",7)
bite = Attack("Bite",6)

#Criaturas

creature1 = Creature("Flameling","Fire",50,10,5,[fireball,scratch])
creature2 = Creature("Aquabub", "Water",55,9,6,[water_blast,bite])

#Iniciar batalha

battle(creature1,creature2)