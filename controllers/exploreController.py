from utils import *
from character import Character
from controllers.battleEventController import BattleEventController

class ExploreController:
    def __init__(self, time, character):
        self.depth = 0
        self.time = time
        self.character = character
        
    def explore(self):
        #get random event based off depth and time
        while True:
            choices = ["Return to town", "Battle"]
            choice = showOptions("What do you do?", choices)
            if (choice == "1"):
                clear()
                write("You return to town to rest")
                break
            if (choice == "2"):
                clear()
                enemy = Character("Goblin", 10, 10, 0)
                battleController = BattleEventController(self.character, enemy)
                battleController.start()
                break

            specialCommands(choice)



