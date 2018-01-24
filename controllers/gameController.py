from utils import *
from character import Character
from controllers.campController import CampController
from controllers.exploreController import ExploreController
import zope.event

class GameController:
    def __init__(self):
        self.character = Character("The hero", 15, 0)
        self.day = 0
        self.timeOfDay = 0
        self.camp = CampController(self.character)

    def playGame(self):
        while True:
            choices = ["Explore into the wilderness",
                "Walk around town"]

            choice = showOptions("What do you do?", choices)
            try:
                value = int(choice)
                if (value == 0): # go explore
                    clear()
                    exploreController = ExploreController(self.timeOfDay, self.hero)
                    exploreController.explore()
                    continue
                elif (value == 1): # Go to camp
                    clear()
                    self.camp.showCamp()
                    continue
            except:
                pass

            # Special commands
            flag = specialCommands(choice)
            if flag == -1:
                break
                