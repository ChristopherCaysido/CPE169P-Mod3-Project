from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('memory.kv')

Window.size = (600,400)

class DropdownWidget(Widget):
    pass

class ProgressBarWidget(Widget):
    pass

class DeckButtonsWidget(Widget):
    pass

class FrontLayout(BoxLayout):
    pass

class MemoryApp(App):
    def build(self):
        frontpage = FrontLayout()
        return frontpage

if __name__=='__main__':
    MemoryApp().run()
