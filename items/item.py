from utils import *
import character

#The item class will contain all the methods needed in order to use items.
#Each item will be represented by a key in a dictionary, and have associated uses
class Item:
    items = {
        "SmallPotion" : {
            "name" : "Small Potion",
            "description" : "A potion that heals small wounds when consumed",
            "actions" : [("Use", "useSmallPotion")]
        }}

    #Item actions return a tuple of (Should consume item, Should count as action)
    @staticmethod
    def useSmallPotion(user, enemy=None):
        # Make sure you dont heal above max health
        health = 5
        if health + user.health > user.maxHealth:
            health = user.maxHealth - user.health

        write(user.name + " drinks the potion and heals for " + str(health))
        user.heal(health)

        return (True, False)

    

