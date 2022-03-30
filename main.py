from kivy.app import App
from kivy import properties as kp
from game.hungryworm import HungryWormGame

class HungryWormApp(App):
    title = kp.StringProperty("Hungry Worm")
    icon = kp.StringProperty("images/Logo.png")

    def build(self):
        return HungryWormGame()

if __name__ == "__main__":
    HungryWormApp().run()
