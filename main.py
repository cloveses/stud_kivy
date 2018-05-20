from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.factory import Factory

class MyForm(BoxLayout):  # 此处类定义虽然为空，但会将my.kv的GUI定义的相关“程序”引入，即相当于在此定义
    text_input = ObjectProperty()   # 在类中添加text_input属性，对应kv文件中用于外部引用的名称，最终指向对应id的GUI部件
    def buttona_act(self):
        print(self.text_input.text) # 获取text_input所指向GUI部件的text值，并打印到控制台

    # 转换界面方法1
    def chg_widget(self):
        self.clear_widgets()
        self.add_widget(Label(text='location')) # 添加程序生成的Widget

    # 转换界面方法2
    def chg_widget2(self):
        self.clear_widgets()
        cur_wdgt = Factory.MyForm2()
        self.add_widget(cur_wdgt)        # 添加kv文件中定义的Widget

class MyApp(App):         # 类名MyApp 在运行时正好自动载入对应的my.kv文件
    pass

MyApp().run()
