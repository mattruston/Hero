from utils import *
from character import Character
from bonuses.bonus import *
from items.item import *

class BattleEventController:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start(self):
        write("As you wonder through the woods, a creature cloaked in shadow appears.")

        #fight loop
        while True:
            if self.checkEnd():
                return

            if self.playerTurn() == -1:
                return

            if self.checkEnd():
                return
                
            self.enemyTurn()

    def playerTurn(self):
        while True:

            #Tick through bonuses
            for bonus in self.character.bonuses:
                bonus.act("PlayerStart", self.character)

            #TODO Add inventory dynamically
            choices = ["Run", "Attack", "Inventory"]
            choice = showOptions("What do you do?", choices)

            if (choice == "1"):
                clear()
                write("In a panic you run from the enemy")
                #For now returning -1 to know that we need to quit
                return -1

            if (choice == "2"):
                clear()
                self.character.attack(self.enemy)
                break

            if (choice == "3"):
                clear()
                if self.useItem():
                    break

            # handle special commands
            flag = specialCommands(choice)

        return 0

    def useItem(self):
        while True:
            choices = []
            for item in self.character.inventory:
                choices += [item.name + "           " + str(item.quantity) + "x"]
            choices += ["Go back"]

            choice = showOptions("Use an item?", choices)

            if choice.isdigit():
                value = int(choice) - 1
                
                if value >= 0 and value < len(self.character.inventory):
                    self.character.inventory[value].use(self.character)
                    return True

                elif value == len(choices) - 1:
                    return False

            specialCommands(choice)

    def enemyTurn(self):
        self.enemy.attack(self.character)

    def checkEnd(self):
        if self.enemy.health <= 0:
            write(self.character.name + " defeats " + self.enemy.name)
            #TODO: present rewards here
            return True

        if self.character.health <= 0:
            write("The darkness engulfs your fire and the world around you fades to black.")
            #TODO: death logic
            return True