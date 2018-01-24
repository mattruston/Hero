from weapons.weapon import Weapon
from armor.armor import Armor

class Character:
    def __init__(self, name, hp, strength, weapon = Weapon(), armor = Armor(), bonuses = [], inventory = [], statuses = []):
        self.name = name
        self.health = hp
        self.strength = strength
        self.weapon = weapon
        self.armor = armor
        self.bonuses = bonuses # all types of bonuses, they handle their own action based on state code
        self.inventory = inventory
        self.statuses = statuses

    def tick(self):
        # go through characters event based effects and allow them to trigger themselves if nessecary
        self.applyBonuses()
        self.applyStatuses()

    def takeDamage(self, damage):
        self.health -= damage

    def heal(self, health):
        self.health += health

    def defend(self, damage):
        return self.armor.defend()