"""Handles interactions between the deck class and the database"""

from deck import Deck
import csv
import sqlite3

class DeckManager:
    def __init__(self, db_path:str = 'memory.db'):
        self.db_path = db_path
        self.decks = {}


    def create_deck(self, name:str, 
                    items:dict=None, 
                    from_csv:str=None, 
                    encoding:str='utf-8-sig')->Deck:
        """Creates a deck named name with items specified in the items dict
        Can also specify a csv file as an alternative for the dictionary
        items takes precedence"""
        if not items and from_csv:
            items = {}
            with open(from_csv, newline='', encoding=encoding) as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) != 2:
                        raise ValueError("Wrong csv format. Each row should contain exactly two items.")
                    items[row[0]] = row[1]
        new_deck = Deck(name, items)

        self.decks[name] = new_deck

        return new_deck

    def load_database(self):

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            for row in cursor.execute("SELECT * FROM decks"):
                cursor.execute("SELECT * FROM deck_items where deck_id = ")
                load_deck = deck(name, items)
                
        self.decks[name] = load_deck  

    def update_database(self):
        
        pass