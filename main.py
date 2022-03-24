
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.metrics import sp

SPRIZE_SIZE = sp(20)
COLS = int(Window.width / SPRIZE_SIZE)
ROWS = int(Window.height / SPRIZE_SIZE)


class HungryWormApp(App):
    def build(self):
        return self.form


if __name__ == '__main__':
    HungryWormApp().run()
