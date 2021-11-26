import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

Window.clearcolor = (.5, .5, 1, .5)

kv = '''
Carousel:
    direction: 'right'

    
    Label:
        text: '한글 0'
        font_size: '40sp'
        font_name: 'GmarketSansTTFBold.ttf' 
    Label:
        text: 'slide 1'
        font_size: '40sp'
    Label:
        text: 'slide 2'
        font_size: '40sp'    
'''


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)


TestApp().run()
