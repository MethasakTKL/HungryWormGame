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
SPRITE_SIZE = sp(25)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)

# set worm lenght and speed
LENGHT = 2
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

class Apple(Sprite):
    pass

class HungryWorm(App):
    sprize_size = kp.NumericProperty(SPRITE_SIZE)

    head = kp.ListProperty([0, 0])
    worm = kp.ListProperty()
    lenght = kp.NumericProperty(LENGHT)

    apple = kp.ListProperty([0, 0])
    apple_sprite = kp.ObjectProperty(Apple)

    direction = kp.StringProperty(UP, options=(LEFT, RIGHT, UP, DOWN))
    buffer_direction = kp.StringProperty(UP, options=(LEFT, RIGHT, UP, DOWN, ''))
    block_input = kp.BooleanProperty(False)

    alpha = kp.NumericProperty(0)

    def on_start(self):
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        Window.bind(on_touch_down=self._on_touch_down)
        Window.bind(on_touch_move=self._on_touch_move)
        self.apple_sprite = Apple()
        self.apple = self.new_apple_location
        self.head = self.new_head_location
        Clock.schedule_interval(self.move, MOVESPEED)

    def on_apple(self, *args):
        self.apple_sprite.coord = self.apple
        if not self.apple_sprite.parent:
            self.root.add_widget(self.apple_sprite)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        try:
            self.try_change_direction(direction_keys[text])
        except KeyError:
            pass

    def _on_touch_down(self, widget, touch):
        self._touch_point = [touch.x, touch.y]

    def _on_touch_move(self, widget, touch):
        if touch.x <= self._touch_point[0] - 50:
            self.try_change_direction(LEFT)
        elif touch.x >= self._touch_point[0] + 50:
            self.try_change_direction(RIGHT)
        elif touch.y >= self._touch_point[1] + 50:
            self.try_change_direction(UP)
        elif touch.y <= self._touch_point[1] - 50:
            self.try_change_direction(DOWN)

    def try_change_direction(self, new_direction):
        if direction_group[new_direction] != direction_group[self.direction]:
            if self.block_input:
                self.buffer_direction = new_direction
            else:
                self.direction = new_direction
                self.block_input = True

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

    @property
    def new_apple_location(self):
        while True:
            apple = [randint(1, dim - 1) for dim in [COLS, ROWS]]
            if apple not in self.worm and apple != self.apple:
                return apple

    def move(self, *args):
        self.block_input = False
        new_head = [sum(x) for x in zip(
            self.head, direction_values[self.direction])]
        if not self.check_in_bounds(new_head) or new_head in self.worm:
            return self.die()
        self.head = new_head
        if new_head == self.apple:
            self.lenght += 1
            self.apple = self.new_apple_location
        if self.buffer_direction:
            self.try_change_direction(self.buffer_direction)
            self.buffer_direction = ''
        self.head = new_head
    
    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))
    
    def die(self):
        self.root.clear_widgets()
        self.alpha = ALPHA
        Animation(alpha=0, duration = MOVESPEED).start(self)

        self.worm.clear()
        self.lenght = LENGHT
        self.apple = self.new_apple_location
        self.head = self.new_head_location


if __name__ == '__main__':
    HungryWorm().run()
