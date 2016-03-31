from django.db import models
from .charspecials import *
from TaleSite.equipment.models import *
import random

SCHOLAR_MIN_MAX_DEFENSE = (-1, 3)
SCHOLAR_MIN_MAX_POWER = (-1, 3)
SCHOLAR_MIN_MAX_HEALTH = (-1, 3)
FIGHTER_MIN_MAX_DEFENSE = (1, 4)
FIGHTER_MIN_MAX_POWER = (1, 4)
FIGHTER_MIN_MAX_HEALTH = (2, 5)
WIZARD_MIN_MAX_POWER = (-1, 3)
WIZARD_MIN_MAX_DEFENSE = (-2, 3)
WIZARD_MIN_MAX_HEALTH = (3, 4)


def get_random(values):
    return random.randint(values[0], values[1])


class Player(models.Model):

    def __init__(self, save_name, codeword):
        super(Player, self).__init__()
        self.save_name = models.CharField(eval(input("Welcome to the game! What is your username? "
                                                     "\Don't worry, you'll determine character names later.")),
                                          max_length=20, unique=True)
        self.codeword = models.CharField(max_length=15)


class Character(models.Model):

    def __init__(self, alias=models.CharField(eval(input("What is your name?")), max_length=20, unique=True),
                 weapon=Weapon(), health=15, strength=10, defense=10, winpoints=0):
        super(Character, self).__init__()
        self.owner = models.ForeignKey(Player)
        self.alias = alias
        self.weapon = weapon
        self.health = health
        self.strength = strength
        self.defense = defense
        self.proficiencies = []
        self.winpoints = winpoints

    def __str__(self):
        return "My name is " + str(self.alias) + ". Prepare yourself."

    def attack(self):
        if self.weapon in self.proficiencies:
            self.hit_strength = self.weapon.attack_power + self.strength
        else:
            self.hit_strength = self.weapon.attack_penalty + self.strength
            if self.hit_strength < 0:
                self.hit_strength = 0

        return self.hit_strength

    def defend(self, enemy):
        if enemy.hit_strength > self.defense:
            damage = enemy.hit_strength - self.defense
            self.health -= damage
        else:
            damage = 0
            self.health = self.health
        return damage


class Wizard(Character):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.health = 15 + get_random(WIZARD_MIN_MAX_HEALTH)
        self.strength = 10 + get_random(WIZARD_MIN_MAX_POWER)
        self.defense = 10 + get_random(WIZARD_MIN_MAX_DEFENSE)
        self.archetype = "Wizard"
        self.proficiencies = ['Wand', 'Staff', 'Broomstick']
        self.special = Pureblood()

    def apply(self):
        self.health += self.special.healbonus
        return self.health


class Mage(Wizard):
    def __init__(self, *args, **kwargs):
        super(Mage, self).__init__(*args, **kwargs)
        self.archetype = "Mage"
        self.proficiencies.append('Sword')


class Shaman(Wizard):
    def __init__(self, *args, **kwargs):
        super(Shaman, self).__init__(*args, **kwargs)
        self.archetype = "Shaman"
        self.proficiencies.extend(['Familiar', 'Knife'])
        self.proficiencies.remove('Broomstick')


class Fighter(Character):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.health = 15 + get_random(FIGHTER_MIN_MAX_HEALTH)
        self.strength = 10 + get_random(FIGHTER_MIN_MAX_POWER)
        self.defense = 10 + get_random(FIGHTER_MIN_MAX_DEFENSE)
        self.archetype = "Fighter"
        self.proficiencies = ['Sword', 'Axe', 'Knife']
        self.special = Thickskin()

    def apply(self):
        self.defense += self.special.defbonus
        return self.defense


class Barbarian(Fighter):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)
        self.archetype = "Barbarian"
        self.proficiencies.extend(['Club', 'WarAxe'])


class Assassin(Fighter):
    def __init__(self, *args, **kwargs):
        super(Assassin, self).__init__(*args, **kwargs)
        self.archetype = "Assassin"
        self.proficiencies.extend(['Dart', 'Poison'])
        self.proficiencies.remove('Axe')


class Scholar(Character):
    def __init__(self, *args, **kwargs):
        super(Scholar, self).__init__(*args, **kwargs)
        self.health = 15 + get_random(SCHOLAR_MIN_MAX_HEALTH)
        self.strength = 10 + get_random(SCHOLAR_MIN_MAX_POWER)
        self.defense = 10 + get_random(SCHOLAR_MIN_MAX_DEFENSE)
        self.archetype = "Scholar"
        self.proficiencies = ['Knife', 'Pen']
        self.special = Cunning()

    def apply(self):
        self.strength += self.special.attbonus
        return self.strength


class Alchemist(Scholar):
    def __init__(self, *args, **kwargs):
        super(Alchemist, self).__init__(*args, **kwargs)
        self.archetype = "Alchemist"
        self.proficiencies.extend(['Bombs', 'Elixirs', 'Poison', 'Hyde'])

