import kivy
kivy.require('2.1.0')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


Builder.load_file("main.kv")

class Proef(BoxLayout):
    pass

class ProefApp(App):

    def build(self):
        return Proef()


if __name__ == '__main__':

    x = ProefApp()
    x.run()


