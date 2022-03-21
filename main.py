from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import *

class Cell(Widget):
    graphical_size = ListProperty([1, 1])
    graphical_pos = ListProperty([1, 1])

    def __init__(self, x, y, size, margin=4):
        super().__init__()
        self.actual_size = (size, size)
        self.graphical_size = (size - margin, size - margin)
        self.margin = margin
        self.actual_pos = (x, y)
        self.attach_worm_body()

    def attach_worm_body(self):
        self.graphical_pos = (self.actual_pos[0] - self.graphical_size[0] / 2, self.actual_pos[1] - self.graphical_size[1] / 2)

class Form(Widget):
    def __init__(self):
        super().__init__()
        self.cell1 = Cell(100, 100, 30)
        self.cell2 = Cell(130, 100, 30)
        self.cell3 = Cell(160, 100, 30)
        self.add_widget(self.cell1)
        self.add_widget(self.cell2)
        self.add_widget(self.cell3)


class HungryWormApp(App):
    def build(self):
        self.form = Form()
        return self.form


if __name__ == '__main__':
    HungryWormApp().run()
