import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Button


class FantasticApp(App):
    def build(self):
        return Button(text='Hello world app')


FantasticApp().run()
