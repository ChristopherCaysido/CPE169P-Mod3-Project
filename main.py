from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty

from deckmanager import DeckManager
from drillmanager import DrillManager

Window.size = (1000,700)
DB_PATH = 'memory.db'



class FrontScreen(Screen):
    def callback_popup(self):
        show_popup()
class DrillScreen(Screen):
    pass
class PopupWidget(FloatLayout):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('memory.kv')
class MemoryApp(App):    
    deck_manager = ObjectProperty(DeckManager(DB_PATH))
    drill_manager = ObjectProperty(DrillManager(DB_PATH))
    current_deck_name = StringProperty('')
    current_deck = ObjectProperty(None)
    current_drill = ObjectProperty(None)
    
    def build(self):
        spinner = kv.ids.frontscreen.ids.spinnerdropdown
        spinner.values = self.get_names()
        spinner.text = spinner.values[0]
        return kv

    
    def get_names(self):
        return self.deck_manager.get_deck_names()
    
    def start_drill(self):
        self.current_deck = self.deck_manager.decks[self.current_deck_name]
        self.current_drill = self.drill_manager.start_drill(self.current_deck)
        if self.current_deck.custom_font:
            self.root.ids.drillscreen.ids.drillQuestion.font_name = self.current_deck.custom_font
        self.load_next_question()
    
    def load_next_question(self):
        self.root.ids.drillscreen.ids.drillQuestion.text = self.current_drill.pop_next_question().text
        
        choices = self.root.ids.drillscreen.ids.choices.children
        choice_texts = self.current_drill.get_choices()
        for choice, choice_text in zip(choices, choice_texts):
            choice.text = choice_text

def show_popup():
    show = PopupWidget()
    popupWindow = Popup(title='Create Deck',content=show,size_hint=(None,None),size=(700,600))
    popupWindow.open()



if __name__=='__main__':
    MemoryApp().run()
