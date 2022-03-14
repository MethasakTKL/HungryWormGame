from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

class HungryWormGame(Widget):
    pass
        

class HungryWormApp(App):
    def build(self):
        game = HungryWormGame()
        return game

if __name__ == '__main__':
    HungryWormApp().run()
