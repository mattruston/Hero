from utils import *
from weapons.weapon import Weapon
from armor.armor import Armor
from items.item import Item

class Character:
    def __init__(self, name, hp, maxHealth, strength, weapon = Weapon("Short Sword"), armor = Armor("Cloth Armor"), bonuses = [], inventory = {}, statuses = [], gold = 0):
        self.name = name
        self.health = hp
        self.maxHealth = maxHealth
        self.strength = strength
        self.weapon = weapon
        self.armor = armor
        self.bonuses = bonuses # all types of bonuses, they handle their own action based on state code
        self.inventory = inventory
        self.statuses = statuses
        self.gold = gold

    def tick(self):
        # go through characters event based effects and allow them to trigger themselves if nessecary
        self.applyBonuses()
        self.applyStatuses()

    def takeDamage(self, damage):
        self.health -= damage
        write(self.name + " has " + str(self.health) + "hp")

    def heal(self, health):
        self.health += health
        write(self.name + " has " + str(self.health) + "hp")

    def defend(self, damage):
        return self.armor.defend(damage)

    def attack(self, target):
        self.weapon.attack(self, target)

    def giveItem(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def removeItem(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1

            if self.inventory[item] == 0:
                del self.inventory[item]

    # Returns true or false if the spend is valid
    def spendGold(self, amount):
        if (self.gold >= amount):
            self.gold -= amount
            return True
        display("You don't have enough gold for that")
        return False

    def openInventory(self, targets=[]):
        while True:
            choices = []
            orderedItemKeys = []
            for item, quantity in self.inventory.items():
                choices += [Item.items[item]["name"] + "           " + str(quantity) + "x"]
                orderedItemKeys += [item]
            choices += ["Go back"]

            choice = showOptions("Use an item?", choices)

            if choice.isdigit():
                value = int(choice) - 1
                
                if value >= 0 and value < len(self.inventory):
                    item = orderedItemKeys[value]

                    #TODO: Show list of all possible actions for an item
                    methodName = Item.items[item]["actions"][0][1]
                    consumed, tookTurn = getattr(Item, methodName)(self)

                    if consumed:
                        self.removeItem(item)

                    return tookTurn

                elif value == len(choices) - 1:
                    return False

            specialCommands(choice)
        