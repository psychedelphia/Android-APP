import kivy
 
kivy.require('2.0.0')
 
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
 
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.imagelist import SmartTileWithLabel
 
Window.size = (563, 1001)
Window.top, Window.left = 30, 700
 
 
class FantasticApp(MDApp):
    def build(self):
        # Phone-like --------------------------------------------------------------
        self.theme_cls.theme_style = "Dark"
        MDs = MDScreen(pos_hint={'right': .995, 'top': .985}, size_hint=(.99, .98),
                       radius=(25, 25, 25, 25), md_bg_color=(1, 1, 1, 1))
        # -------------------------------------------------------------------------
 
        MDgl = MDGridLayout(cols=1, adaptive_height=True, padding=(25, 0), spacing=5)
 
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image01.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 1[/size]\n[size=14]image01.jpg[/size]'))
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image02.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 2[/size]\n[size=14]image02.jpg[/size]'))
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image03.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 3[/size]\n[size=14]image03.jpg[/size]'))
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image04.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 4[/size]\n[size=14]image04.jpg[/size]'))
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image05.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 5[/size]\n[size=14]image05.jpg[/size]'))
        MDgl.add_widget(SmartTileWithLabel(
                              source='./image06.jpg', size_hint_y=None, height=200,
                              text='[size=26]Image 6[/size]\n[size=14]image06.jpg[/size]'))
 
        sv = ScrollView()
        sv.add_widget(MDgl)
        MDs.add_widget(sv)
        return MDs
 
 
FantasticApp().run()
