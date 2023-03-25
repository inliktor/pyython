from random import *
class Hero():
    def __init__(self,name,health,armor,power,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Привет',self.name)
        print('Здоровье',self.health)
        print('Броня:', self.armor)
        print('Сила:',self.power)
        print('Алебарда:', self.weapon)

class Enemy():
    def __init__(self,name,health,armor,power,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Привет',self.name)
        print('Здоровье',self.health)
        print('Броня:', self.armor)
        print('Сила:',self.power)
        print('нож:', self.weapon)

class Battle:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        while self.hero.health > 0 and self.enemy.health > 0:
            # Герой атакует злодея
            enemy_damage = self.hero.power + self.hero.weapon.get('Урон', 0) - self.enemy.armor

            self.enemy.health -= enemy_damage
            print(f"{self.hero.name} атакует {self.enemy.name} и наносит {enemy_damage} ед. урона.")
            if self.enemy.health <= 0:
                print(f"{self.hero.name} побеждает {self.enemy.name}!")
                break

            # Злодей атакует героя
            hero_damage = self.enemy.power + self.enemy.weapon.get('Урон', 0) - self.hero.armor
            self.hero.health -= hero_damage
            print(f"{self.enemy.name} атакует {self.hero.name} и наносит {hero_damage} ед. урона.")
            if self.hero.health <= 0:
                print(f"{self.enemy.name} побеждает {self.hero.name}!")
                break

knight = Hero('Густав', randint(30,100), randint(1,50), randint(1,80), {'Урон': randint(1,70)})
knight.print_info()

print('__________________________________________\n')

evil = Enemy('Бенедикт', randint(15,70), randint(1,61), randint(1,50), {'Урон': randint(1,60)})
evil.print_info()

print('__________________________________________\n')

battle = Battle(knight, evil)
battle.start()
