import json

class Creature:
    def __init__(self,name,type_,level):
        self.name = name
        self.type = type_
        self.level = level
    
    def to_dict(self):
        return{
            "name" : self.name,
            "type" : self.type,
            "level" : self.level
        }

class Pokedex:
    def __init__(self):
        self.creatures = []
    
    def add_creatures(self,creature):
        self.creatures.append(creature)
        print(f"{creature.name} foi adicionado à Pokédex!")
    
    def list_creatures(self):
        if not self.creatures:
            print("Nenhuma criatura cadastrada.")
            return
    
        print("\n Pokédex: ")
        for c in self.creatures:
            print(f"{c.name} / Tipo: {c.type} / Nível{c.level}")
    
    def search_by_name(self,name):
        results = [c for c in self.creatures if name.lower() in c.name.lower()]

        if results:
            print("\n Resultados: ")
            for c in results:
                print(f"{c.name} / Tipo: {c.type} / Nível{c.level}")
        else:
            print("Nenhuma criatura encontrada.")
        
    def filter_by_type(self,type_):
        results = [c for c in self.creatures if c.type.lower() == type.lower()]

        if results:
            print(f"\n Criaturas do tipo {type_}: ")
            for c in results:
                print(f"{c.name} Nível: {c.level}")
        else:
            print("Nenhuma criatura desse tipo.")
    
    def save_to_file(self, filename="pokedex.json"):
        data = [c.to_dict() for c in self.creatures]
        with open(filename, "w") as f:
            json.dump(data,f,indent = 4)
            print("Pokédex salva com sucesso!")
    
    def load_from_file(self,filename="pokedex.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.creatures = [Creature(d["name"],d["type"],d["level"])for d in data]
                print("Pokédex carregada!")
        except FileNotFoundError:
            print("Arquivo não encontrado, começando nova Pokédex.")

#===== MENU INTERATIVO =====

def main():
    pokedex = Pokedex()
    pokedex.load_from_file()

    while True:
        print("\n ===== MENU ===== ")
        print("1. Adicionar criatura")
        print("2. Listar criaturas")
        print("3. Buscar por nome")
        print("4. Filtrar por tipo")
        print("5. Salvar")
        print("6. Sair")

        choice = input("Escolha: ")

        if choice == "1":
            name = input("Nome: ")
            type = input("Tipo: ")
            level = int(input("Nível: "))
            pokedex.add_creatures(Creature(name,type_,level))
        
        elif choice == "2":
            pokedex.list_creatures()
        
        elif choice == "3":
            name = input("Nome para buscar: ")
            pokedex.search_by_name(name)
        
        elif choice == "4":
            type_ = input("Tipo: ")
            pokedex.filter_by_type(type_)
        
        elif choice == "5":
            pokedex.save_to_file()
        
        elif choice == "6":
            pokedex.save_to_file()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()