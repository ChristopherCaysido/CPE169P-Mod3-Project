import random

class Deck:
    def __init__(self, name: str = '', items: dict = {}, custom_font:str = ''):
        self.name = name
        self.items = {key: Item(key, item) for key, item in items.items()}
        self.custom_font = custom_font

    def draw_items(self, k: int = 10 ):
        '''Draws k number of item/s from deck'''
        return random.sample(list(self.items.values()), k = k)
                # weights = [item.weight for item in self.items.items()])
    
    def draw_answers(self, k: int = 4):
        '''Draws k number of answer/s from the deck'''
        return [item.answer for item in random.sample(list(self.items.values()), k = k)]

    def add_item(self, text: str, answer: str):
        self.items[text] = Item(text, answer)

    def __getitem__(self, key: str):
        return self.items[key]

    # def update_weights(self, items):
    #     '''Updates the weights of the items in the deck'''
    #     for key in items: 
    #         self.items[key].weight = items[key]

class Item:
    def __init__(self, text = '', answer = '', weight = 0):
        self.text = text
        self.answer = answer
        # self.weight = weight

    def check_answer(self, answer):
        return self.answer == answer

    def __str__(self):
        return f'{self.text}: {self.answer}'

    __repr__ = __str__