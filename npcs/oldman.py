from npcs.npc import NPC
from utils import *
from random import randint

class Oldman(NPC):
    def __init__(self):
        super().__init__("Old man", "Talk to the old man")

    def run(self, character):
        options = [(0,"Say 'hi'"), (1,"Walk away")]
        clear()
        optionID = dialogueOptions("You walk up to the old man. What do you do?", options)
        if (optionID == 0):
            self.firstDialogue(character)
            return
        elif (optionID == 1):
            clear()
            return

    def firstDialogue(self, character):
        clear()
        write("\nOld man: Hello there stranger.\n")
        options = [(1, "Ask: 'who are you?"), (0,"Ask: 'what are you doing in my camp?'"), (2,"Walk away")]
        while True:
            optionID = dialogueOptions("How do you respond?", options)
            if (optionID == 0):
                self.secondDialogueOption1(character)
                return
            elif (optionID == 1):
                self.secondDialogueOption2(character)
                index = indexOfOption(1, options)
                options.pop(index)
                options.insert(len(options) - 2, (3, "Ask: 'can you help me?"))
                continue
            elif (optionID == 3):
                self.adviceDialogue(character)
                index = indexOfOption(3, options)
                options.pop(index)
                continue
            else:
                clear()
                return
    
    def secondDialogueOption1(self, character):
        clear()
        write("Old man: Your camp! Sonny back in my day these woods were only ruled by the tree sprites. Nasty little buggers but at least they were more polite than you!")
        write("The Old man walks away from you in a huff.\n")
        return

    def secondDialogueOption2(self, character):
        clear()
        write("Old man: I'm just a simple old man.\n")
        return

    def adviceDialogue(self, character):
        clear()
        advice = ["You can get help by typing 'help or 'h' at any time.", "You can end the day and heal by visiting your tent."]
        tipIndex = randint(0, len(advice))
        write("Old man: " + advice[tipIndex])
        clear()

