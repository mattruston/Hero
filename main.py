import os
import time
import sys

def sleep(t):
    time.sleep(t)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def write(string):
    for c in string:
        sleep(0.05)
        sys.stdout.write(c)
        sys.stdout.flush()

        if c == ".":
           sleep(0.25) 

    sleep(0.5)
    print("")


def showOptions(choices) -> int:
    write("What do you do?")

    for x in range(len(choices)):
        display(str(x) + ". " + choices[x])

    while True:
        choice = input("> ")
        sleep(0.3)

        try:
            value = int(choice)
            if (value >= 0 and value < len(choices)):
                return value
        except:
            pass

        display("Invalid command") 


def display(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sleep(0.5)
    print("")

class Armor:
    def __init__(self):
        pass

    def defend(self, damage):
        return damage - 1

class Weapon:
    def __init__(self):
        pass

    def attack(self, attacker, target):
        #base sword
        damage = attacker.strength + 1
        damage = target.armor.defend()
        target.takeDamage(damage)
        display(attacker.name + " slices " + target.name + " for " + damage + " damage!")

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

    def defend(self, damage):
        return self.armor.defend()

class GameController:
    def __init__(self):
        self.hero = Character("The hero", 15, 0)
        self.gameState = 0
        self.timeOfDay = 0

    def playGame(self):
        while True:
            choices = ["Explore into the wilderness",
                "Walk around town"]

            choice = showOptions(choices)

            if (choice == 0):
                clear()
                write("As the darkness surrounds you, you fall to the floor. You died.")
            elif (choice == 1):
                clear()
                write("Nothing is here.")
                # dont actually do this recursive
                pass

def main():
    clear()

    write("You awaken next to your fire. The flames dance with the encroaching darkness. You pick up your sword.")
    gameController = GameController()
    gameController.playGame()
    

if __name__ == "__main__":
    main()