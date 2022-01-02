import kivy

kivy.require('2.0.0')

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class FantasticApp(MDApp):
    def build(self):
        return MDFlatButton(text='test')


FantasticApp().run()
