from utils import *
from character import Character
from bonuses.bonus import *
from items.item import *
from controllers.eventController import EventController

class BattleEventController(EventController):
    def __init__(self, character, enemy):
        super().__init__(character, "You must fight to survive!")
        self.enemy = enemy

    def run(self):

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
            choices = ["Attack", "Inventory", "Run"]
            choice = showOptions("What do you do?", choices)

            if (choice == "1"):
                clear()
                self.character.attack(self.enemy)
                break

            if (choice == "2"):
                clear()
                if self.useItem():
                    break
                continue

            if (choice == "3"):
                clear()
                write("In a panic you run from the enemy")
                #For now returning -1 to know that we need to quit
                return -1

            # handle special commands
            flag = specialCommands(choice)

        return 0

    def useItem(self):
        return self.character.openInventory()

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
            kill()
            return True