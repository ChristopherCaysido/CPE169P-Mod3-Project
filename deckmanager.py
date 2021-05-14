"""Handles interactions between the deck class and the database"""

from deck import Deck
import csv
import sqlite3

class DeckManager:
    def __init__(self, db_path:str = 'memory.db'):
        self.db_path = db_path
        self.decks = {}
        self.create_database()

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

    def create_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS decks (
                            deck_id INTEGER PRIMARY KEY,
                            deck_name TEXT UNIQUE,
                            custom_font_path TEXT)""")
            cur.execute("""CREATE TABLE IF NOT EXISTS deck_items (
                            item_id INTEGER PRIMARY KEY,
                            deck_id INTEGER NOT NULL,
                            item_text TEXT NOT NULL UNIQUE,
                            item_answer TEXT NOT NULL,
                            FOREIGN KEY (deck_id)
                                REFERENCES decks (deck_id))""")
            cur.execute("""CREATE TABLE IF NOT EXISTS drills (
                            drill_id INTEGER PRIMARY KEY,
                            deck_id INTEGER NOT NULL,
                            number_right_answers INTEGER NOT NULL,
                            number_items INTEGER NOT NULL,
                            date TEXT,
                            FOREIGN KEY (deck_id)
                                REFERENCES decks (deck_id))""")
            

    def load_database(self):

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM decks")
            for deck_id, name, custom_font in cursor.fetchall():
                
                cursor.execute("""SELECT item_text, item_answer  
                                    FROM deck_items where deck_id = ?""", 
                                deck_id)
                items = {item[0]: item[1] for item in cursor.fetchall()}
                load_deck = Deck(name, items, custom_font)
                self.decks[name] = load_deck  

    def update_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for deck in self.decks.values():
                cursor.execute('''REPLACE INTO decks (name, custom_font_path)
                                    VALUES (?, ?)''',
                                (deck.name, deck.custom_font))
                cursor.execute('SELECT deck_id FROM decks WHERE deck_name = ?', (deck.name,))
                id = cursor.fetchall()[-1][0]
                for item in deck.items.values():
                    cursor.execute('''REPLACE INTO deck_items (deck_id, item_text, item_answer)
                                        VALUES (?, ?, ?)''',
                                    (id, item.text, item.answer))
                
            
