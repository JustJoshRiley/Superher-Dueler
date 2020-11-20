from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()

        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health

        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):

        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):

        defense = self.defend()
        damage_taken = damage - defense
        if damage_taken < 0:
            damage_taken = 0
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return 0
        
        while opponent.is_alive() and self.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

        if opponent.is_alive():
            print(f"{opponent.name} won!")

            opponent.add_kill(1)
            self.add_death(1)


        elif self.is_alive():
            print(f"{self.name} won!")

            self.add_kill(1)
            opponent.add_death(1)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths






if __name__ == "__main__":
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.abilities)
    # print(hero.attack())
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())