from utils import *
from character import Character

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
            try:
                value = int(choice)
                if (value == 0):
                    clear()
                    write("As the darkness surrounds you, you fall to the floor. You died.")
                    continue
                elif (value == 1):
                    clear()
                    write("Nothing is here.")
                    continue
            except:
                pass

            # Special commands
            if choice == "quit" or choice == "q":
                clear()
                write("The darkness engulfs your fire and the world around you fades to black.")
                break
            elif choice == "help" or choice == "h":
                display("\nHero's Diary:\n-------------\nTaking an action:\n\tYou can input a choice by submitting the correct action number\nExiting the game:\n\tYou can quit the game at anytime by typing 'quit' or 'q'\n")
            else:
                write("That is not an action.")
                