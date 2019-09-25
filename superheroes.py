import random

def inputCheck(input, input_type):
    if input.isalpha():
        

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
    def __init__(self, name, starting_health = 100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.status = "Alive"
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage_amt):
        self.current_health -= (damage_amt - self.defend())
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    
    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        
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
                opponent.add_kill(1)
                self.add_deaths(1)
                self.status = "Dead"
                opponent.status = "Alive"
                print(opponent.name + " won!")
                fighting = False
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_deaths(1)
                opponent.status = "Dead"
                self.status = "Alive"
                print(self.name + " won!")
                fighting = False
            else:
                continue

class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0
                
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        alive_hero_list_1 = []
        alive_hero_list_2 = []

        for hero_1 in self.heroes:
                if hero_1.status == "Alive":
                    alive_hero_list_1.append(self.heroes.index(hero_1))
        
        for hero_2 in other_team.heroes:
                if hero_2.status == "Alive":
                    alive_hero_list_2.append(other_team.heroes.index(hero_2))

        while len(alive_hero_list_1) > 0 and len(alive_hero_list_2) > 0:
            random_hero_1 = self.heroes[random.choice(alive_hero_list_1)]
            random_hero_2 = other_team.heroes[random.choice(alive_hero_list_2)]

            random_hero_1.fight(random_hero_2)

            for hero_alivecheck_1 in self.heroes:
                if hero_alivecheck_1.status == "Dead":
                    alive_hero_list_1.pop(self.heroes.index(hero_alivecheck_1))
            
            for hero_alivecheck_2 in other_team.heroes:
                if hero_alivecheck_2.status == "Dead":
                    alive_hero_list_2.pop(other_team.heroes.index(hero_alivecheck_2))
        
        if len(alive_hero_list_1) > 0:
            print("Team " + self.name + " won!")
        elif len(alive_hero_list_2) > 0:
            print("Team " + other_team.name + " won!")
        elif len(alive_hero_list_1) == len(alive_hero_list_2):
            print("Draw!")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            print("Hero: " + hero.name + "| Kills: " + hero.kills + "| Deaths: " + hero.deaths)
    
class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):
        input("Enter Ability Name: ")
        input("Enter Ability Attack Strength: ")

if __name__ == "__main__":
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    print(team_two.heroes[0].current_health)

    team_one.attack(team_two)

    print(team_two.heroes[0].current_health)