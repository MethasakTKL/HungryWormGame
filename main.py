from kivy.app import App
from kivy import properties as kp
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from collections import defaultdict
from random import randint

''' 
Code Understanding

head: worm's head position 
body: worm's body position
head_sprite: graphic of the head
ิbody_sprite: graphic of the body

- We keep position in this in list size 2 and change to coordinate x-axis and y-axis [0, 0]
- We get a value of position and change it in to graphic "sprite"

Explain Graphic Algorithm 
-- When get variable [x, y] -->  Display variables on screen at position [x, y].

'''

SPRITE_SIZE = sp(25)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)

# GAME Default Settings
DEFAULT_LENGHT = 2    # Starting Worm Lenght
MOVESPEED = .15       # Game Speed
ALPHA = .5

# set directions
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

direction_group = {
    LEFT: 'horizontal',
    RIGHT: 'horizontal',
    UP: 'vertical',
    DOWN: 'vertical'
}

direction_keys = {
    'a': LEFT,
    'd': RIGHT,
    'w': UP,
    's': DOWN
}

class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

SPRITES = defaultdict(lambda: Sprite())

class WormHead(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

class Apple(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

class HungryWorm(App):
    icon = './images/Logo.png'
    image_source = kp.StringProperty("images/Headup.png")

    # Worm Section
    sprize_size = kp.NumericProperty(SPRITE_SIZE)
    
    head = kp.ListProperty([0, 0])
    head_sprite = kp.ObjectProperty(WormHead)

    body = kp.ListProperty()
    lenght = kp.NumericProperty(DEFAULT_LENGHT)

    # Apple Section
    apple = kp.ListProperty([0, 0])
    apple_sprite = kp.ObjectProperty(Apple)

    # Direction Section
    direction = kp.StringProperty(UP, options=(LEFT, RIGHT, UP, DOWN))
    buffer_direction = kp.StringProperty(UP, options=(LEFT, RIGHT, UP, DOWN, ''))
    block_input = kp.BooleanProperty(False)

    alpha = kp.NumericProperty(0)

    # When the app start
    def on_start(self):
        
        # Initialize game input
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        Window.bind(on_touch_down=self._on_touch_down)
        Window.bind(on_touch_move=self._on_touch_move)

        # Load sounds
        self.playtime_sound = SoundLoader.load("sounds/Backsound.mp3")
        self.die_sound = SoundLoader.load('sounds/die.wav')
        self.eat_sound = SoundLoader.load('sounds/eat.wav')
        self.playtime_sound.loop = True
        self.playtime_sound.play()
        
        self.apple_sprite = Apple()
        self.head_sprite = WormHead()
        self.apple = self.new_apple_location # spawn apple
        self.head = self.new_head_location # spawn worm
        Clock.schedule_interval(self.move, MOVESPEED) # setting fps in game

    # Head Position 
    def on_head(self, *args):
        self.body = self.body[-self.lenght:] + [self.head]

    # Body Position
    def on_body(self, *args):
        for index, coord in enumerate(self.body):
            if coord == self.head:
                self.head_sprite.coord = coord

                if not self.head_sprite.parent:
                    self.root.add_widget(self.head_sprite)

            else:
                sprite = SPRITES[index]
                sprite.coord = coord
                if not sprite.parent:
                    self.root.add_widget(sprite)

    # Setting Apple when start
    def on_apple(self, *args):
        self.apple_sprite.coord = self.apple
        if not self.apple_sprite.parent:
            print("Spawn Apple")
            self.root.add_widget(self.apple_sprite)

    # Needed by Window.request_keyboard
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    # Keyboard input handler
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        try:
            self.try_change_direction(direction_keys[text])
        except KeyError:
            pass

    # Touchscreen input handler
    def _on_touch_down(self, widget, touch):
        self._touch_point = [touch.x, touch.y]

    # Touchscreen input handler
    def _on_touch_move(self, widget, touch):
        if touch.x <= self._touch_point[0] - 50:
            self.try_change_direction(LEFT)
        elif touch.x >= self._touch_point[0] + 50:
            self.try_change_direction(RIGHT)
        elif touch.y >= self._touch_point[1] + 50:
            self.try_change_direction(UP)
        elif touch.y <= self._touch_point[1] - 50:
            self.try_change_direction(DOWN)

    # Change Worm Movement Direction
    def try_change_direction(self, new_direction):
        if direction_group[new_direction] != direction_group[self.direction]:
            if self.block_input:
                self.buffer_direction = new_direction
            else:
                self.direction = new_direction
                self.block_input = True
            
            # Change direction of head graphic
            if new_direction == LEFT:
                self.image_source = "images/Headleft.png"
            elif new_direction == RIGHT:
                self.image_source = "images/Headright.png"
            elif new_direction == UP:
                self.image_source = "images/Headup.png"
            elif new_direction == DOWN:
                self.image_source = "images/Headdown.png"

    # Function spawn Head in Random position
    @property
    def new_head_location(self):
        return [randint(2, dim - 2) for dim in [COLS, ROWS]]

    # Fucntion spawn Apple in Random position
    @property
    def new_apple_location(self):
        while True:
            new_apple = [randint(1, dim - 1) for dim in [COLS, ROWS]]
            if new_apple not in self.body and new_apple != self.apple:
                return new_apple

    # Function Move for worm
    def move(self, *args):
        self.block_input = False

        new_head = [sum(x) for x in zip(
            self.head, direction_values[self.direction])]

        # Check postion worm if [ In bounds ] or [ Collide itself ] --> Die
        if not self.check_in_bounds(new_head) or new_head in self.body:
            return self.die()

        # If Head's position on Apple's position --> +1 Lenght
        if new_head == self.apple:
            self.lenght += 1
            self.apple = self.new_apple_location
            self.eat_sound.play()

        if self.buffer_direction:
            self.try_change_direction(self.buffer_direction)
            self.buffer_direction = ''

        self.head = new_head
    
    # Function check worm out of screen --> Die
    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))
    
    # Function Die --> reset lenght, body, apple and Spawn Snake in new position
    def die(self):
        # Play die sound
        self.die_sound.play()
        
        # Clear widget
        for index, coord in enumerate(self.body):
                sprite = SPRITES[index]
                sprite.coord = coord
                self.root.remove_widget(sprite)
        self.apple_sprite.clear_widgets()
        self.body.clear()

        # Red screen effect
        self.alpha = ALPHA
        Animation(alpha=0, duration=MOVESPEED).start(self)

        # Reset value of game
        self.lenght = DEFAULT_LENGHT
        self.apple = self.new_apple_location
        self.head = self.new_head_location

if __name__ == '__main__':
    HungryWorm().run()
