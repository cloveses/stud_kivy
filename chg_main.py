from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.factory import Factory

class MyForm(BoxLayout): 
    text_input = ObjectProperty()
    def buttona_act(self):
        print(self.text_input.text) 

    def chg_widget(self):
        self.clear_widgets()
        self.add_widget(Label(text='location')) 

    def chg_widget2(self):
        self.clear_widgets()
        cur_wdgt = Factory.MyForm2()
        self.add_widget(cur_wdgt) 

class MyForm2(BoxLayout):

    def chg_widget3(self):
        self.clear_widgets()
        cur_wdgt = Factory.MyForm()
        self.add_widget(cur_wdgt)


class MychgApp(App):
    def build(self):
        return MyForm()

MychgApp().run()
