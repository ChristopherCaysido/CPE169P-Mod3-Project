"""Handles interactions between the deck class and the database"""

import deck
import csv
import sqlite3

class DeckManager:
    def create_deck(name, items=None, from_csv=None):
        """Creates a deck named name with items specified in the items dict
        Can also specify a csv file as an alternative for the dictionary
        items takes precedence"""
        if not items and from_csv:
            items = {}
            with open(from_csv, newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) != 2:
                        raise ValueError("Wrong csv format. Each row should contain exactly two items.")
                    items[row[0]] = row[1]
        
        deck.Deck(name, items)