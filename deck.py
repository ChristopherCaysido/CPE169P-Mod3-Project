

class Deck:
    def __init__(self, name=None, items=None):
        self.name = name
        self.items = items 

    def draw(self):
        pass

class Item:
    def __init__(self):
        self.text