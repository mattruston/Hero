from npcs.npc import NPC

class Oldman(NPC):
    def __init__(self, name, option):
        super().__init__(name, option)
        self.actions = {}

    def run(self, character):
        
