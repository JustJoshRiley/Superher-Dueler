from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:

            #Randomly select a living hero from each team (hint: look up what random.choice does)
            current_hero = choice(living_heroes)
            hero_deaths = current_hero.deaths

            #Randomly select a living hero from each team (hint: look up what random.choice does)
            current_opponent = choice(living_opponents)
            opponent_deaths = current_opponent.deaths

            # have the heroes fight each other
            current_hero.fight(current_opponent)

            # update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if hero_deaths < current_hero.deaths:
                living_heroes.remove(current_hero)
            elif opponent_deaths < current_opponent.deaths:
                living_opponents.remove(current_opponent)


    def remove_hero(self, name):
        
        foundHero = False
        for hero in self.heroes:

            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
