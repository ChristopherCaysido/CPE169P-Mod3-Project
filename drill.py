
from deck import Deck
from deck import Item
import datetime
import random


class Drill:
    def __init__(self, deck: Deck, k:int=10):
        self.deck = deck
        self.questions = self.deck.draw_items(k)
        self.question_queue = self.questions.copy()
        self.scores = {} # might use for weights for drawing items from deck
        self.current_question = None
        self.date = datetime.datetime.now() 

    def pop_next_question(self) -> Item:
        self.current_question = self.question_queue.pop()
        return self.current_question

    def get_choices(self, k = 4):
        choices = self.deck.draw_answers(k)
        answer = self.current_question.answer

        if answer not in choices:
            choices.pop()
            choices.append(answer)
        
        random.shuffle(choices)

        return choices

    def check_answer(self, answer):
        '''Checks the answer is correct for the current question.
        If not correct, the current question is inserted to the back of the question queue'''
        correct = self.current_question.check_answer(answer)
        text = self.current_question.text
        if text not in self.scores:
            self.scores[text] = 0
        if correct:
            self.scores[text] += 1
        else:
            self.scores[text] += -1
            self.question_queue.insert(0, self.current_question)
        
        return correct

    def is_question_queue_empty(self):
        return not len(self.question_queue)

