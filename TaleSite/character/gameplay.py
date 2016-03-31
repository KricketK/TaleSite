from django.db import models
from .models import *

begin = True
character = False

print("Welcome to the arena!")

while begin:
    path = eval(input('What path do you choose? \n 1. Fighter \n 2. Wizard \n 3. Scholar'))

    try:
        path = int(path)
    except ValueError:
        print("Try using the designating number, Stupid. \n")

    else:

        if int(path) == 1:
            print("So you're a tough-guy, huh?")
            player = Fighter(eval(input("What's your name?")))
            begin = False
            character = True

        if int(path) == 2:
            print("I'm watching you, magic user.")
            player = Wizard(eval(input("What's your name?")))
            begin = False
            character = True

        if int(path) == 3:
            print("You're rather scrawny. Are you lost?")
            player = Scholar(eval(input("What's your name?")))
            begin = False
            character = True

        if 0 > int(path) > 3:
            print("Oh a special snowflake, eh? \n")

print(("Good luck, " + player.name + " the " + player.archetype + ". You will need it."))

while character:
    print(("You are proficient in: " + str(player.proficiencies)))

    weapon_choice = eval(input("Pick your weapon:\n1. Sword\n2. Axe\n3. Knife\n4. Wand\n5. Staff\n6. Broomstick\n"
                              "7. Pen\n"))
    try:
        weapon_choice = int(weapon_choice)
    except ValueError:
        print("You need a weapon before you may enter")

    if weapon_choice == 1:
        player.weapon = Sword()
    elif weapon_choice == 2:
        player.weapon = Axe()
    elif weapon_choice == 3:
        player.weapon = Knife()
    elif weapon_choice == 4:
        player.weapon = Wand()
    elif weapon_choice == 5:
        player.weapon = Staff()
    elif weapon_choice == 6:
        player.weapon = Broomstick()
    elif weapon_choice == 7:
        player.weapon = Pen()
    if 0 < weapon_choice < 8:
        print(("You have chosen to carry a " + str(player.weapon) + " into battle."))
        character = False
    elif 0 > weapon_choice > 7:
        print("You need a weapon before you may enter.")

maxhealth = player.health
winpoints = 0

print((eval(input("Now that you are outfitted, take stock of your abilities. To access your abilities type in 'Myself' "
                "at any time."))))
Myself = ("Name: " + player.name + "\nClass: " + player.archetype + "\nYour health is, " + str(player.health) +
         "\nYour attack power is " + str(player.strength) + "\nYour defense is " + str(player.defense) +
         "\nYour weapon is a " + str(player.weapon) + "\nYou currently have " + str(winpoints) + "points")

Myself = str(Myself)

print(Myself)
