import random

# Class for Ability that defines what an Ability is
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    
    # Attack method to return an attack value between 0 and the input value
    def attack(self):
        return random.randint(0, self.attack_strength)

# Class for Armor that defines what Armor is
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    # Block method to return a block value between 0 and the input value
    def block(self):
        return random.randint(0, self.max_block)

# Class for Hero that defines what a Hero is
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
    
    # Method that adds the inputed ability to the Hero's list of abilities
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    # Method that adds the inputed weapon to the Hero's list of weapons
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    # Method that adds the inputed armor to the Hero's list of armors
    def add_armor(self, armor):
        self.armors.append(armor)
    
    # Method that uses the Ability class' Attack method and returns the sum of all abilities "attack"
    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack
    
    # Method that uses the Armor class' Block method and returns the sum of all armors "block"
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    '''
    Method that calculates damage by subtracting the total block from the damage amount and
    then subtracts that from the Hero's current health
    '''
    def take_damage(self, damage_amt):
        self.current_health -= (damage_amt - self.defend())
    
    # Method that checks if the Hero is still alive or not by checking their current health
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    
    # Method that counts how many kills a Hero has
    def add_kill(self, num_kills):
        self.kills += num_kills

    # Method that counts how many deaths a Hero has
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
    
    '''
    Method that handles a fight between two Heros. If neither Hero has abilites, it is considered a "draw".
    Otherwise, it runs through each attack, defend, and damage calculation function. It then checks which
    Hero is still alive and adds kills and deaths respectively and also prints the name of the winner.
    '''
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

# Class that defines what a Weapon is; inherits the same properities as an Ability but uses its own attack function
class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)

# Class that defines what a Team is
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    # Method that accepts a Hero name input and removes them from the Team; if the Hero isn't found, returns "0"
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0
                
    # Method that prints the name of each Hero on the Team
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    # Method that accepts a Hero name input and adds them to the Team
    def add_hero(self, hero):
        self.heroes.append(hero)

    '''
    Method that handles a fight between two Teams. First, it checks to see which Heroes are "alive" on each Team and then
    appends their index to a new list. Then, a Hero is randomly selected by index from both lists to fight. After the fight
    is complete, a check occurs to see which Hero died and removes their index from the respective list. Repeats until one
    Team has no more Heros alive and then returns the name of the winning Team. In the case both Teams have zero Heroes
    alive at the same time, it returns a "draw".
    '''
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
            return self.name
        elif len(alive_hero_list_2) > 0:
            return other_team.name
        elif len(alive_hero_list_1) == len(alive_hero_list_2):
            return "Draw!"

    # Method that revives all Heros on a Team to the inputted starting health or the default "100"
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            hero.status = "Alive"

    # Method that prints the stats of each Hero on the inputted Team
    def stats(self):
        for hero in self.heroes:
            print("Hero: " + hero.name + " | Kills: " + str(hero.kills) + " | Deaths: " + str(hero.deaths))

# Class that defines what the Arena is (essentially character creation + fighting)    
class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
        self.winning_team = None
    
    # Method that accepts user input to create abilities
    def create_ability(self):
        name = input("Enter Ability Name: ")
        strength = int(input("Enter Ability Attack Strength: "))
        ability = Ability(name, strength)
        return ability
    
    # Method that accepts user input to create weapons
    def create_weapon(self):
        name = input("Enter Weapon Name: ")
        strength = int(input("Enter Weapon Attack Strength: "))
        weapon = Weapon(name, strength)
        return weapon
    
    # Method that accepts user input to create armors
    def create_armor(self):
        name = input("Enter Armor Name: ")
        block_power = int(input("Enter Blocking Strength: "))
        armor = Armor(name, block_power)
        return armor
    
    # Method that accepts user input to create Heroes, also calls previous three functions for each Hero
    def create_hero(self):
        name = input("Enter Hero Name: ")
        health = int(input("Enter Hero Health: "))
        hero = Hero(name, health)

        ability_creation = True
        while ability_creation:
            ability_option = input("Create ability? (Y/N): ").lower()
            if ability_option == "y":
                ability = self.create_ability()
                hero.add_ability(ability)
            else:
                ability_creation = False
        
        weapon_creation = True
        while weapon_creation:
            weapon_option = input("Create weapon? (Y/N): ").lower()
            if weapon_option == "y":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            else:
                weapon_creation = False
        
        armor_creation = True
        while armor_creation:
            armor_option = input("Create armor? (Y/N): ").lower()
            if armor_option == "y":
                armor = self.create_armor()
                hero.add_armor(armor)
            else:
                armor_creation = False
        
        return hero
    
    # Method that accepts user input to create the first Team
    def build_team_one(self):
        name = input("Team 1 Name: ")
        num_of_heroes = int(input("How many heroes?: "))
        self.build_team_one = Team(name)

        for i in range(num_of_heroes):
            hero = self.create_hero()
            self.build_team_one.add_hero(hero)
        
        self.build_team_one.view_all_heroes()
    
    # Method that accepts user input to create the second Team
    def build_team_two(self):
        name = input("Team 2 Name: ")
        num_of_heroes = int(input("How many heroes?: "))
        self.build_team_two = Team(name)

        for i in range(num_of_heroes):
            hero = self.create_hero()
            self.build_team_two.add_hero(hero)
        
        self.build_team_two.view_all_heroes()
    
    # Method that has the two teams fight each other
    def team_battle(self):
        self.winning_team = self.build_team_one.attack(self.build_team_two)
    
    # Method that prints who won the fight and the stats of each Hero on both teams; also shows any surviving Heroes
    def show_stats(self):
        print("The winners are: " + self.winning_team)
        
        self.build_team_one.stats()
        self.build_team_two.stats()

        if self.winning_team == self.build_team_one.name:
            for hero in self.build_team_one.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)
        elif self.winning_team == self.build_team_two.name:
            for hero in self.build_team_two.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ").lower()

        #Check for Player Input
        if play_again == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()