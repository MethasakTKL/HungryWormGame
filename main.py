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
SPRITE_SIZE = sp(20)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)

# set worm lenght and speed
LENGHT = 3
MOVESPEED = .1
ALPHA = .5

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
direction_group = {LEFT: 'horizontal',
                   UP: 'vertical',
                   RIGHT: 'horizontal',
                   DOWN: 'vertical'
}
direction_keys = {'a': LEFT, 
                  'w': UP,
                  'd': RIGHT,
                  's': DOWN}

class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

SPRITES = defaultdict(lambda: Sprite())
class Worm(App):
    sprize_size = kp.NumericProperty(SPRITE_SIZE)

    head = kp.ListProperty([0, 0])
    worm = kp.ListProperty()
    lenght = kp.NumericProperty(LENGHT)

    food = kp.ListProperty([0, 0])

    direction = kp.StringProperty(UP, options=(LEFT, RIGHT, UP, DOWN))

    alpha = kp.NumericProperty(0)

    def on_start(self):
        self.head = self.new_head_location
        Clock.schedule_interval(self.move, MOVESPEED)
        Window.bind(on_keyboard = self.key_handler)

    def key_handler(self, _, __, ___, key, *____):
        try:
            self.try_change_direction(direction_keys[key])
        except KeyError:
            pass

    def try_change_direction(self, new_direction):
        if direction_group[new_direction] != direction_group[self.direction]:
           self.direction = new_direction

    def on_head(self,*args):
        self.worm = self.worm[-self.lenght:] + [self.head]

    def on_worm(self,*args):
        for index, coord in enumerate(self.worm):
            sprite = SPRITES[index]
            sprite.coord = coord
            if not sprite.parent:
                self.root.add_widget(sprite)

    @property
    def new_head_location(self):
        return [randint(2, dim - 2) for dim in [COLS, ROWS]]

    def move(self, *args):
        new_head = [sum(x) for x in zip(
            self.head, direction_values[self.direction])]
        if not self.check_in_bounds(new_head):
            return self.die()
        self.head = new_head
    
    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))
    
    def die(self):
        self.alpha = ALPHA
        Animation(alpha=0, duration = MOVESPEED).start(self)
        self.worm.clear()
        self.root.clear_widgets()
        self.head = self.new_head_location


if __name__ == '__main__':
    Worm().run()
