from drill import Drill
from deck import Deck


class DrillManager:
    def __init__(self, db_path:str = 'memory.db'):
        self.db_path = db_path
        self.current_drill = None
    
    def start_drill(self, deck: Deck, k: int = 10):
        if(len(deck.items) < k):
            k = len(deck.items)
        self.current_drill = Drill(deck, k)
        return self.current_drill

    def end_drill(self):
        # save results of current drill to database
        # name of deck, score and date
        # self.update_database()
        self.current_drill = None

    def update_database(self):
        pass