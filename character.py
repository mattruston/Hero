from utils import *
from weapons.weapon import Weapon
from armor.armor import Armor

class Character:
    def __init__(self, name, hp, maxHealth, strength, weapon = Weapon("Short Sword"), armor = Armor("Cloth Armor"), bonuses = [], inventory = [], statuses = [], gold = 0):
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
        self.inventory.append(item)

    # Returns true or false if the spend is valid
    def spendGold(self, amount):
        if (self.gold >= amount):
            self.gold -= amount
            return True
        display("You don't have enough gold for that")
        return False
        