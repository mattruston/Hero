from utils import *
import character

class Weapon:
    def attack(self, attacker, target):
        #base sword
        damage = attacker.strength + 1
        damage = target.defend(damage)
        damage = 1
        display(attacker.name + " slices " + target.name + " for " + str(damage) + " damage!")
        target.takeDamage(damage)