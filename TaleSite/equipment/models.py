from TaleSite.character.models import Player
from django.db import models
import random


class Weapon(models.Model):
    def __init__(self, written=str()):
        super(Weapon, self).__init__()
        self.attack_power = 0
        self.attack_penalty = 0
        self.written = written
        self.owner = models.ForeignKey(Player)

    def __str__(self):
        return self.written


class OpenHand(Weapon):
    def __init__(self):
        super(OpenHand, self).__init__()
        self.attack_power = -5
        self.attack_penalty = 0
        self.written = "None"

    def __str__(self):
        return self.written


class Club(Weapon):
    def __init__(self):
        super(Club, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 0
        self.written = 'Club'

    def __str__(self):
        return self.written


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()
        self.attack_power = 5
        self.attack_penalty = 1
        self.written = 'Sword'

    def __str__(self):
        return self.written


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 1
        self.written = 'Axe'

    def __str__(self):
        return self.written


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 1
        self.written = 'Knife'

    def __str__(self):
        return self.written


class Dart(Weapon):
    def __init__(self):
        super(Dart, self).__init__()
        self.attack_power = 2
        self.attack_penalty = 1
        self.written = 'Dart'

    def __str__(self):
        return self.written


class Poison(Weapon):
    def __init__(self):
        super(Poison, self).__init__()
        self.attack_power = random.randint(1, 5)
        self.attack_penalty = 3
        self.written = 'Poison'

    def __str__(self):
        return self.written


class Pen(Weapon):
    def __init__(self):
        super(Pen, self).__init__()
        self.attack_power = 1
        self.attack_penalty = 0
        self.written = 'Pen'

    def __str__(self):
        return self.written


class Staff(Weapon):
    def __init__(self):
        super(Staff, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 0
        self.written = 'Staff'

    def __str__(self):
        return self.written


class Wand(Weapon):
    def __init__(self):
        super(Wand, self).__init__()
        self.attack_power = 2
        self.attack_penalty = 1
        self.written = 'Wand'

    def __str__(self):
        return self.written


class Bombs(Weapon):
    def __init__(self):
        super(Bombs, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 4
        self.written = 'Bombs'

    def __str__(self):
        return self.written


class Elixirs(Weapon):
    def __init__(self):
        super(Elixirs, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 2
        self.written = 'Elixirs'

    def __str__(self):
        return self.written


class Hyde(Weapon):
    def __init__(self):
        super(Hyde, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 4
        self.written = 'Hyde'

    def __str__(self):
        return self.written


class Familiar(Weapon):
    def __init__(self):
        super(Familiar, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 3
        self.written = 'Familiar'

    def __str__(self):
        return self.written


class Broomstick(Weapon):
    def __init__(self):
        super(Broomstick, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 1
        self.written = 'Broomstick'

    def __str__(self):
        return self.written


class GreatSword(Weapon):
    def __init__(self):
        super(GreatSword, self).__init__()
        self.attack_power = 8
        self.attack_penalty = 4
        self.written = 'Great Sword'

    def __str__(self):
        return self.written


class WarAxe(Weapon):
    def __init__(self):
        super(WarAxe, self).__init__()
        self.attack_power = 8
        self.attack_penalty = 3
        self.written = 'War Axe'

    def __str__(self):
        return self.written


def pickweapon():
    weaponlist = [Club, Sword, Axe, Knife, Broomstick, Pen, Staff, Wand, Pen]
    random.randint(0, len(weaponlist)-1)
    randweapon = weaponlist[random.randint(0, len(weaponlist)-1)]()
    return randweapon