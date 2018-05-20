from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen

class MyForm(BoxLayout):  # 此处类定义虽然为空，但会将my.kv的GUI定义的相关“程序”引入，即相当于在此定义
    text_input = ObjectProperty()   # 在类中添加text_input属性，对应kv文件中用于外部引用的名称，最终指向对应id的GUI部件
    btnc_chg = ObjectProperty()

    def buttona_act(self):
        print(self.text_input.text) # 获取text_input所指向GUI部件的text值，并打印到控制台

class MyForm2(BoxLayout):
    btnd_chg = ObjectProperty()

class MyApp(App):         # 类名MyApp 在运行时正好自动载入对应的my.kv文件
    
    def build(self):
        myform = MyForm()
        myform.btnc_chg.bind(on_press=self.chgc)
        myform2 = MyForm2()
        myform2.btnd_chg.bind(on_press=self.chgd)
        

MyApp().run()
