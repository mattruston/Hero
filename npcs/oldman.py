from npcs.npc import NPC
from utils import *

class Oldman(NPC):
    def __init__(self, name, option):
        super().__init__(name, option)
        self.actions = {}

    def run(self, character):
        options = [(0,"Say 'hi'"), (1,"Walk away")]
        while True:
            clear()
            optionID = dialogueOptions("You walk up to the old man. What do you do?", options)
            if (optionID == 0):
                firstDialogue(character)
                return
            elif (optionID == 1):
                clear()
                return

# NEED A NEW SHOW OPTIONS THAT CAN TAKE A DICTIONARY WITH ID'S
# This way we can remove options from the list and have them complete all of the interacts
def firstDialogue(character):
    clear()
    write("\nOldman: Hello there stranger.\n")
    options = [(0,"Ask: 'what are you doing in my camp?'"), (1, "Ask: 'who are you?"), (2,"Walk away")]
    while True:
        optionID = dialogueOptions("How do you respond?", options)
        if (optionID == 0):
            secondDialogueOption1(character)
            return
        elif (optionID == 1):
            secondDialogueOption2(character)
            index = indexOfOption(1, options)
            options.pop(index)
            continue
        else:
            clear()
            return
    
def secondDialogueOption1(character):
    clear()
    write("Oldman: Minding my own business! Unlike you.")
    write("The Old man walks away from you in a huff.\n")
    return

def secondDialogueOption2(character):
    clear()
    write("Oldman: I'm just a simple old man.\n")
    return
