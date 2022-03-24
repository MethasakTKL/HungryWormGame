from kivy import properties as kp
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import sp
from kivy.uix.button import Button
from kivy.uix.widget import Widget

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


class HungryWormApp(App):
    head = kp.ListProperty([0, 0])
    worm = kp.ListProperty()

    food = kp.ListProperty([0, 0])

    def on_start(self):
        Clock.schedule_interval(self.move, MOVESPEED)



        


if __name__ == '__main__':
    HungryWormApp().run()
