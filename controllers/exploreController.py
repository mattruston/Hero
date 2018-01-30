from utils import *
from character import Character
from controllers.battleEventController import BattleEventController
from npcs.cultist import Cultist
from controllers.dialogueEventController import DialogueEventController
from random import randrange

class ExploreController:
    def __init__(self, time, character):
        self.depth = 0
        self.time = time
        self.character = character
        cultist = Cultist()
        cultistEvent = DialogueEventController(self.character, "As you set off into the surrounding forest, you see a cloaked figure in the trees.", cultist)
        self.events = [cultistEvent]
        
    def explore(self):
        distance = 0
        while True:
            if (distance >= 12 or distance > len(self.events)):
                clear()
                write("While you continue walking you see you are near the edge of the forest.")
                write("As soon as you clear the treeline you find your self standing at the edge of what seems to be an endless cliff staring out over a dark abyss, you have nowhere to go.")
                write("You return to your camp unharmed")
                return
            eventIndex = randrange(len(self.events)) # random event chosen
            currentEvent = self.events[eventIndex]
            choices = ["Return to town", currentEvent.eventOption()]
            write(currentEvent.eventIntro())
            choice = showOptions("What do you do?", choices)
            if (choice == "1"):
                clear()
                write("You return to town to rest")
                return
            if (choice == "2"):
                # clear()
                # enemy = Character("Goblin", 10, 10, 0)
                # battleController = BattleEventController(self.character, enemy)
                # battleController.run()
                currentEvent.run()
                distance = distance + 1
                self.events.pop(eventIndex)
                continue

            specialCommands(choice)



