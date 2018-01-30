from controllers.eventController import EventController

#wrapper around the NPC's run to adhere to EventController
class DialogueEventController(EventController):
    def __init__(self, character, intro, npc):
        super().__init__(character, intro)
        self.npc = npc
        self.intro = intro
        self.option = npc.option

    def run(self):
        # write(self.intro)
        self.npc.run(self.character)

    def eventOption(self):
        return self.option