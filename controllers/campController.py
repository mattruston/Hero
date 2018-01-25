from utils import *
from npcs.npc import NPC

class CampController:
    def __init__(self, people = []):
        self.people = people
        self.addPerson(NPC('Old Man', 'Talk to the old man'))

    def showCamp(self, character):
        while True:
            if (len(self.people) == 0):
                write("There is no one here yet.")
                return

            options = [x.option for x in self.people] + ["Go to your tent."]

            choice = showOptions("What do you do?", options)

            if (choice.isdigit()):
                choice = int(choice) - 1
                if (choice >= 0 and choice < len(self.people)):
                    self.people[choice].run(character) # Run the persons interaction
                    continue
                elif (choice == len(self.people)):
                    self.tent(character)
                    continue
            
            # handle special commands
            flag = specialCommands(choice)

    def addPerson(self, person):
        self.people.append(person)

    def tent(self, character):
        clear()
        health = int(character.health*.25)
        write("You have a good nights rest and heal for " + str(health))
        character.heal(health)
