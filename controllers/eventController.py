class EventController:
    def __init__(self, character):
        self.character = character

    def run(self):
        write("An event has begun")