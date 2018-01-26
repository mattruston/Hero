from utils import *
import character

class Item:
    def __init__(self, quantity = 1):
        self.name = "item"
        self.quantity = quantity
        self.description = "A quick description of the item"

    def use(self, user):
        print("The item was used")

class SmallPotion(Item):
    def __init__(self, quantity = 1):
        #TODO Use supercall here or something nicer
        self.name = "Small Potion"
        self.quantity = quantity
        self.description = "A potion that heals small wounds when consumed"

    def use(self, user):
        #TODO move this handling to inventory
        if self.quantity <= 0:
            return

        # Make sure you dont heal above max health
        health = 5
        if health + user.health > user.maxHealth:
            health = user.maxHealth - user.health

        write(user.name + " drinks the potion and heals for " + str(health))
        user.heal(health)

        self.quantity -= 1

