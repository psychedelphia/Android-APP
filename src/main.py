import kivy
 
kivy.require('2.0.0')
 
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
 
 
class FantasticApp(App):
    _init_mic = 0
    _init_sec = 0
    _init_min = 0
    _lab_items = 1
    _lab_list = []
 
    def _bt_start(self, bt_instance):
        if bt_instance.text == 'Start':
            # call _clock_call() every 0.01 seconds
            self.event = Clock.schedule_interval(self._clock_call, 0.01)
            bt_instance.text = 'Stop'
        else:
            self.event.cancel()
            bt_instance.text = 'Start'
 
 
    def _bt_lab(self, bt_instance):
        if FantasticApp._lab_items < 11:
            lab_items = '{}: {:0>2}:{:0>2}.{:0>2}'.format(FantasticApp._lab_items,
                                                          str(FantasticApp._init_min),
                                                          str(FantasticApp._init_sec),
                                                          str(FantasticApp._init_mic))
            bt_lab = Button(text=lab_items)
            FantasticApp._lab_list.append(bt_lab)
            self.bl_root.add_widget(bt_lab)
            FantasticApp._lab_items += 1
        else:
            self.bt3.text = 'Max: You can not add the widget'
 
    def _bt_reset(self, bt_instance):
        for i in FantasticApp._lab_list:
            self.bl_root.remove_widget(i)
 
        FantasticApp._lab_list.clear()
        self.bt2.text = '00:00.00'
        self.bt3.text = 'Lab List'
        FantasticApp._init_mic = 0
        FantasticApp._init_sec = 0
        FantasticApp._init_min = 0
        FantasticApp._lab_items = 1
 
    def _clock_call(self, clock_instance):
        self.bt2.text = '{:0>2}:{:0>2}.{:0>2}'.format(str(FantasticApp._init_min),
                                                      str(FantasticApp._init_sec),
                                                      str(FantasticApp._init_mic))
        FantasticApp._init_mic += 1
        if FantasticApp._init_mic > 99:
            FantasticApp._init_mic = 0
            FantasticApp._init_sec += 1
            if FantasticApp._init_sec > 59:
                FantasticApp._init_sec = 0
                FantasticApp._init_min += 1
                if FantasticApp._init_min > 59:
                    # max: 1 hour
                    FantasticApp._init_mic = 0
                    FantasticApp._init_sec = 0
                    FantasticApp._init_min = 0
 
    def build(self):
        # You can make this APP using CLASS
        # start and stop
        bt_top1 = Button(text='Start')
        bt_top1.bind(on_press=self._bt_start)
 
        # Lab
        bt_top2 = Button(text='Lap')
        bt_top2.bind(on_press=self._bt_lab)
 
        bl_top = BoxLayout(size_hint=(1, None), height=150)
        bl_top.add_widget(bt_top1)
        bl_top.add_widget(bt_top2)
 
        # reset
        bt1 = Button(text='Reset', size_hint=(1, None), height=150,
                     on_press=self._bt_reset)
 
        # time
        self.bt2 = bt2 = Button(text='00:00.00', size_hint=(1, None),
                                height=150, font_size=50)
 
        # Lab List
        self.bt3 = bt3 = Button(text='Lab List')
 
        # root BoxLayout
        self.bl_root = bl_root = BoxLayout(orientation='vertical')
        bl_root.add_widget(bl_top)
        bl_root.add_widget(bt1)
        bl_root.add_widget(bt2)
        bl_root.add_widget(bt3)
 
        return bl_root
 
 
FantasticApp().run()
 
