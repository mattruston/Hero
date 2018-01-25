from utils import *
from character import Character
from controllers.campController import CampController
from controllers.exploreController import ExploreController

class GameController:
    def __init__(self):
        self.character = Character("The hero", 15, 0)
        self.day = 0
        self.timeOfDay = 0
        self.camp = CampController()

    def playGame(self):
        characterInfo(self.character)
        while True:
            choices = ["Explore into the wilderness",
                "Walk around town"]

            choice = showOptions("What do you do?", choices)
            if (choice == "0"): # go explore
                clear()
                exploreController = ExploreController(self.timeOfDay, self.character)
                exploreController.explore()
                continue
            elif (choice == "1"): # Go to camp
                clear()
                self.camp.showCamp(self.character)
                continue

            # Special commands
            specialCommands(choice)
                