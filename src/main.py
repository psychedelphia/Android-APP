import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.clearcolor = (.6, 1, .8, 1)
Window.size = (563, 1001)
Window.top, Window.left = 30, 800


class FantasticApp(App):
    def _ti_validate(self, ti_instance):
        self.bt.text = self.ti.text

    def build(self):
        bl = BoxLayout(orientation='vertical')

        self.ti = ti = TextInput()
        self.bt = bt = Button(text='aaa',
                    on_press=self._ti_validate)

        bl.add_widget(ti)
        bl.add_widget(bt)

        return bl


FantasticApp().run()
