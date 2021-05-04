import random

class Deck:
    def __init__(self, name='', items={}):
        self.name = name
        self.items = items 

    def draw_item(self):
        '''Draws an item from deck'''
        return random.choice(self.items.items(), 
                            weights = [item.weight for item in self.items.items()])
    
    def draw_answer(self, n)
        '''Draws an n number of answers/s from the deck'''
        pass

    def update_weights(self, items):
        '''Updates the weights of the items in the deck'''
        for key in items: 
            self.items[key].weight = items[key]

class Item:
    def __init__(self, text = '', answers = [], weight = 0):
        self.text = text
        self.answers = answers
        self.weight = weight