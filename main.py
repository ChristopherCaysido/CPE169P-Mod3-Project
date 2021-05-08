from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

Window.size = (1000,700)

class FrontLayout(FloatLayout):
    def callback_popup(self):
        show_popup()
    
    
class PopupWidget(FloatLayout):
    pass

class MemoryApp(App):
    def build(self):
        frontpage = FrontLayout()
        return frontpage

def show_popup():
    show = PopupWidget()
    popupWindow = Popup(title='Create Deck',content=show,size_hint=(None,None),size=(700,600))
    popupWindow.open()



if __name__=='__main__':
    MemoryApp().run()
