from utils import *
from npcs.npc import NPC
from npcs.oldman import Oldman

class CampController:
    def __init__(self, people = []):
        self.people = people
        self.addPerson(Oldman('Old Man', 'Talk to the old man'))

    def showCamp(self, character):
        while True:

            options = ["Go to your tent."] + [x.option for x in self.people] + ["Go back"]

            choice = showOptions("You walk into your camp. What do you do?", options)

            if (choice.isdigit()):
                choice = int(choice)
                # tent is always first, and options start with 1
                npcChoice = choice - 2

                # User chose resting
                if (choice == 0):
                    self.tent(character)
                    continue

                # User talked to an npc
                elif (npcChoice >= 0 and npcChoice < len(self.people)):
                    self.people[npcChoice].run(character) # Run the persons interaction
                    continue
                # Last option, we return to camp
                elif (npcChoice == len(self.people)):
                    clear()
                    break
            
            # handle special commands
            flag = specialCommands(choice)

    def addPerson(self, person):
        self.people.append(person)

    def tent(self, character):
        clear()
        health = int(character.maxHealth*.25)

        # Make sure you dont heal above max health
        if health + character.health > character.maxHealth:
            health = character.maxHealth - character.health

        write("You have a good nights rest and heal for " + str(health))
        display("")
        character.heal(health)
