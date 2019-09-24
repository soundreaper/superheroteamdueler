import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    
    def attack(self):
        return random.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, current_health):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = 100
        self.current_health = current_health
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += Ability.attack(ability)
        return total_attack

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())