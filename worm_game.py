from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class HungryWormGame(Widget):
    def __init__(self):
        super().__init__()

        with self.canvas:
            self.snake = Rectangle(pos=(10, 10), size=(100, 100))
        

class HungryWormApp(App):
    def build(self):
        game = HungryWormGame()
        return game

if __name__ == '__main__':
    HungryWormApp().run()
