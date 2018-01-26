from utils import *
from character import Character
from bonuses.bonus import *

class BattleEventController:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start(self):
        write("As you wonder through the woods, a creature cloaked in shadow appears.")

        #fight loop
        while True:
            self.playerTurn()
            self.enemyTurn()

    def playerTurn(self):
        while True:
            if self.checkEnd():
                return

            #Tick through bonuses
            for bonus in self.character.bonuses:
                bonus.act("PlayerStart", self.character)

            choices = ["Run", "Attack", "Test bonus"]
            choice = showOptions("What do you do?", choices)

            if (choice == "1"):
                clear()
                write("In a panic you run from the enemy")
                return

            if (choice == "2"):
                clear()
                self.character.attack(self.enemy)
                break

            # handle special commands
            flag = specialCommands(choice)

    def enemyTurn(self):
        if self.checkEnd():
            return

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