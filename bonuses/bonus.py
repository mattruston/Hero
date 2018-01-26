import character
from utils import *

class Bonus:
    def act(self, status, *args):
        print(status)
        print(args)

class HealingAmulet(Bonus):
    def act(self, status, *args):
        if status == "PlayerStart":
            character = args[0]
            if character.health < character.maxHealth:
                display(character.name + "'s Healing Amulet heals for 1")
                character.heal(1)
