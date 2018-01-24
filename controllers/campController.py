from utils import *
from npcs.npc import NPC

class CampController:
    def __init__(self, character, people = []):
        self.character = character
        self.people = people
        self.addPerson(NPC('Old Man', 'Talk to the old man'))

    def showCamp(self):
        while True:
            if (len(self.people) == 0):
                write("There is no one here yet.")
                return

            options = [x.option for x in self.people] + ["Go to your tent."]

            choice = showOptions("What do you do?", options)
            try:
                value = int(choice)
                if (value >= 0 and value < len(self.people)):
                    self.people[value].run() # Run the persons interaction
                    continue
                elif (value == len(self.people)):
                    self.tent()
                    continue
            except:
                pass
            
            # handle special commands
            flag = specialCommands(choice)
            if flag == -1:
                break

    def addPerson(self, person):
        self.people.append(person)

    def tent(self):
        health = int(self.character.health*.25)
        write("You have a good nights rest and heal for " + str(health))
        self.character.heal(health)
