class Armor:
    def __init__(self, name):
        self.name = name
        
    def defend(self, damage):
        return damage - 1