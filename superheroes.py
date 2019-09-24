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
    def __init__(self, name, current_health = 100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.current_health = current_health
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += Ability.attack(ability)
        return total_attack
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += Armor.block(armor)
        return total_block
    
    def take_damage(self, damage_amt):
        self.current_health -= (damage_amt - self.defend())
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
        
    def fight(self, opponent):
        fighting = True
        while fighting == True:
            if self.abilities == None:
                return "Draw"
                fighting = False
            
            hero1_attack = self.attack()
            hero2_attack = opponent.attack()

            hero1_defense = self.defend()
            hero2_defense = opponent.defend()

            self.take_damage(hero2_attack)
            opponent.take_damage(hero1_attack)

            if self.is_alive() == False:
                print(opponent.name + " won!")
                fighting = False
            elif opponent.is_alive() == False:
                print(self.name + " won!")
                fighting = False
            else:
                continue

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 20)
    ability2 = Ability("Super Eyes", 20)
    ability3 = Ability("Wizard Wand", 20)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)