from utils import *
from character import Character

class BattleEventController:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start(self):
        write("As you wonder through the woods, a creature cloaked in shadow appears.")
        while True:
            choices = ["Run", "Attack"]
            choice = showOptions("What do you do?", choices)
            if (choice == "0"):
                clear()
                write("In a panic you run from the enemy")
                break
            if (choice == "1"):
                clear()
                self.character.attack(self.enemy)

            if self.checkEnd():
                return

            self.enemyTurn()

            if self.checkEnd():
                return

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