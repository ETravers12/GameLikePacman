import arcade
import pathlib

class Pacman(arcade.Window):

    def __init__(self):
        super().__init__("Pacman", 640, 640)

        # initialize the player
        self.player = None

    def setup(self):
        # setup the player
        self.player = arcade.AnimatedTimeSprite()

    def update(self, delta_time: float):

    def on_draw(self):

    def on_key_press(self, key: int, modifiers: int):

    def on_key_release(self):


def main():
    window: Pacman = Pacman
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()