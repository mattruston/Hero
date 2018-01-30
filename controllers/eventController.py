class EventController:
    def __init__(self, character, intro):
        self.character = character

    def run(self):
        write("An event has begun")

    def eventIntro(self):
        return self.intro

    