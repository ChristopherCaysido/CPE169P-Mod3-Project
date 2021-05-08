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

Window.size = (1000,700)


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
    def build(self):
        return kv

def show_popup():
    show = PopupWidget()
    popupWindow = Popup(title='Create Deck',content=show,size_hint=(None,None),size=(700,600))
    popupWindow.open()



if __name__=='__main__':
    MemoryApp().run()
