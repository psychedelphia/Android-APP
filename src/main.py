import kivy
 
kivy.require('2.0.0')
 
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
 
Window.clearcolor = (.6, 1, .8, 1)
Window.size = (563, 1001)
Window.top, Window.left = 30, 800
 
 
class TestApp(App):
    def build(self):
        fl = FloatLayout()
 
        # using canvas
        ta = Line(width=10, cap='none', joint='round', close='False',
                  rectangle=(200, 500, 163, 300))
        fl.canvas.add(Color(0, .5, 0, 1))
        fl.canvas.add(ta)
 
        return fl
 
 
TestApp().run()
 
