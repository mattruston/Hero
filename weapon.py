class Weapon:
    def __init__(self):
        pass

    def attack(self, attacker, target):
        #base sword
        damage = attacker.strength + 1
        damage = target.armor.defend()
        target.takeDamage(damage)
        display(attacker.name + " slices " + target.name + " for " + damage + " damage!")