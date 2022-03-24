
from tkinter import W
from kivy.app import App
from kivy.metrics import sp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import properties as kp
from kivy.uix.widget import Widget
from collections import defaultdict
from kivy.animation import Animation
from random import randint

# set size of window
SPRIZE_SIZE = sp(20)
COLS = int(Window.width / SPRIZE_SIZE)
ROWS = int(Window.height / SPRIZE_SIZE)

# set worm lenght and speed
LENGTH = 3
MOVESPEED = .1

# set direction
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

direction_values = {
    LEFT: [-1, 0],
    RIGHT: [1, 0],
    UP: [0, 1],
    DOWN: [0, -1]
}


class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

SPRITES = defaultdict(lambda: Sprite())
class HungryWormApp(App):
    head = kp.ListProperty([0, 0])
    worm = kp.ListProperty()

    food = kp.ListProperty([0, 0])

    direction = kp.schedule_interval(UP, options=(LEFT, RIGHT, UP, DOWN))

    def on_start(self):
        Clock.schedule_interval(self.move, MOVESPEED)

    def on_head(self):
        self.worm.append(self.head)

    def on_worm(self):
        for index, coord in enumerate(self.worm):
            sprite = SPRITES[index]
            sprite.coord = coord
            if not sprite.parent:
                self.root.add_widget(sprite)

    def move(self):
        new_head = [sum(x) for x in zip(
            self.head, direction_values[self.direction])]
        self.head = new_head


if __name__ == '__main__':
    HungryWormApp().run()
