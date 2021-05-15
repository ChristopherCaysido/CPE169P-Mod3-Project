from deck import Deck
from deckmanager import DeckManager
from drillmanager import DrillManager


if __name__ == '__main__':
    print(Deck('Test Deck'))
    deck_man = DeckManager()
    test_deck = deck_man.create_deck('Test', from_csv='test.csv')
    
    test_deck_de = deck_man.create_deck('Deutsch', from_csv='test_de.csv')
    print(test_deck.items)
    print(list(test_deck_de.items.values()))
    print(deck_man.get_deck_names())

    drill_man = DrillManager()
    dr = drill_man.start_drill(test_deck, 3)
    
    for i in range(3):
        q = dr.pop_next_question()
        print(f'Question: {q.text}')
        print(f'Choices: {dr.get_choices()}')
    