from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class Cell(Widget):
    def __init__(self, x, y, size):
        super().__init__()
        self.size = (size, size)
        self.pos = (x, y)

class Form(Widget):
    def __init__(self):
        super().__init__()
        self.cell = Cell(100, 100, 30)
        self.add_widget(self.cell)


class HungryWormApp(App):
    def build(self):
        self.form = Form()
        return self.form


if __name__ == '__main__':
    HungryWormApp().run()
