from utils import *
from character import Character
from controllers.campController import CampController
from controllers.exploreController import ExploreController
from bonuses.bonus import *
from items.item import *

class GameController:
    def __init__(self):
        self.character = Character("The hero", 15, 15, 0)#, bonuses = [HealingAmulet()])
        self.character.inventory = [SmallPotion(1)]
        self.day = 0
        self.timeOfDay = 0
        self.camp = CampController()

    def playGame(self):
        characterInfo(self.character)
        while True:
            choices = ["Explore into the wilderness",
                "Walk around town"]

            choice = showOptions("What do you do?", choices)

            if (choice == "1"): # go explore
                clear()
                exploreController = ExploreController(self.timeOfDay, self.character)
                exploreController.explore()
                continue
            elif (choice == "2"): # Go to camp
                clear()
                self.camp.showCamp(self.character)
                continue

            # Special commands
            specialCommands(choice)
                