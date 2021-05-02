from kivy.app import app
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class DropdownWidget(Widget):
    pass

class ProgressBarWidget(Widget):
    pass

class DeckButtonsWidget(Widget):
    pass

class FrontLayout(BoxLayout):
    pass

class MemorizationApp(App):
    def build(self):
        frontpage = FrontLayout()
        return frontpage

if __name__=='__main__':
    MemorizationApp().run()
