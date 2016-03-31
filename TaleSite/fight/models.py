from django.db import models
from RPG.character.models import Character
from RPG.equipment.models import Weapon

# Create your models here.


def playerattack(user, enemy):
    damagegiven = enemy.defend(user)
    return damagegiven


def opponentattack(user, enemy):
    damagereceived = user.defend(enemy)
    return damagereceived


def fight(player, opponent):

    maxhealth = player.health
    rounds = 0

    while player.health > 0 and opponent.health > 0:
        rounds += 1

        if player.health > 0:
            givedamage = playerattack(player, opponent)
            print((player.name + " deals " + str(givedamage) + " against " + opponent.name + ". " + opponent.name +
                   "'s health is now " + str(opponent.health)))

        if opponent.health > 0:
            takedamage = opponentattack(player, opponent)
            print((opponent.name + " deals " + str(takedamage) + " against " + player.name + ". " + player.name +
                   "'s health is now " + str(player.health)))

        if player.health <= 0:
            print("Oh dear. Lost another newbie. Bring out the next contender!")

        if opponent.health <= 0:
            print("Hah. You made it. I'm surprised. On to the next round with you!")
            player.health = maxhealth
            player.winpoints += 1

        if rounds > 10:
                if opponent.health < player.health:
                    print("Well, they're not dead, but they aren't getting up either. Good job.")
                    player.health = maxhealth
                    player.winpoints += 1
                    opponent.health = 0
                else:
                    player.health = 0
                    print("The audience can't take any more of this. Get out and let the professionals fight.")
