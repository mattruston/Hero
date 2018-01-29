from controllers.eventController import EventController

#wrapper around the NPC's run to adhere to EventController
class DialogueEventController(EventController):
    def __init__(self, character, npc):
        super().__init_(character)
        self.npc = npc

    def run(self):
        self.npc.run(self.character)
