from utils import *

class NPC:
    def __init__(self, name, option):
        self.name = name
        self.option = option
    
    def run(self, character):
        while True:
            options = ["Say 'hi'", "Walk away"]
            choice = showOptions("What do you do?", options)
            if (choice == "0"):
                write(self.name + ": Hello there stranger.")
                continue
            elif (choice =="1"):
                clear()
                return

            # Special commands
            specialCommands(choice)