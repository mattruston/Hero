from npcs.npc import NPC
from utils import *
from character import Character
from controllers.battleEventController import BattleEventController

class Cultist(NPC):
    def __init__(self):
        super().__init__("Cultist", "Approach to the hooded figure")
        self.body = Character("Cultist", 20, 20, 2)

    def run(self, character):
        clear()
        options = [(0, "Bow back"), (1,"Walk away")]
        optionID = dialogueOptions("You approach the figure, it turns toward you an softly bows. What do you do?", options)
        if (optionID == 0):
            self.hello(character)
            return
        elif (optionID == 1):
            clear()
            return

    def hello(self, character):
        clear()
        options = [(0, "Tell me more about your 'Leto'"), (1, "There's no Sun God. You sound crazy."), (2, "Nothing, I'm just going on my way.")]
        optionID = dialogueOptions(self.name + ": Hello, how may the Sun God Leto be of service to you today?\nHow do you respond?", options)
        if (optionID == 0):
            clear()
            self.offering(character)
        elif (optionID == 1):
            # Start a fight with him, if you win you can earn the item he gives + gold + exp
            clear()
            write(self.name + ": How dare you insult the all-mighty Leto!")
            write("The cultist draws his blade and swings at you!")
            battleController = BattleEventController(character, self.body)
            battleController.run()
        elif (optionID == 2):
            write(self.name + ": A blessed day to you.")
            return  

    def offering(self, character):
        write("....")
        options = [(0, "Give the cultist an offering of 25g"), (1, "Say: 'Sorry i'm all out of cash'")]
        while True:
            optionID = dialogueOptions(self.name + ": Would you be willing to give a small donation to the Church of Leto, everything helps us spread our faith?", options)
            if (optionID == 0):
                # Give him 25g
                if(character.spendGold(25)):
                    character.giveItem("Amulet of the Sun")
                    return
            elif (optionID == 1):
                # too bad
                write(self.name + ": That's too bad.")
                return      
