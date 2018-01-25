from utils import *

class NPC:
    def __init__(self, name, option):
        self.name = name
        self.option = option
    
    def run(self, character):
        while True:
            options = ["Say 'hi'", "Walk away"]
            choice = showOptions("What do you do?", options)
            try:
                value = int(choice)
                if (value == 1):
                    write(self.name + ": Hello there stranger.")
                    continue
                elif (value == 2):
                    clear()
                    return
            except:
                pass

            # Special commands
            specialCommands(choice)