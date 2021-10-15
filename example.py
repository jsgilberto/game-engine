import pygame as pg
from engine.scene import Scene
from engine.game_loop import GameLoop


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


class Game:
    def __init__(self):

        pg.init()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption("Window title")

        # Instantiate base game objects here

        # scene
        self.scene = Scene(
            # add your initial game objects here
            [],
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
        )

        # Instantiate the game loop here
        self.game_loop = GameLoop(limit_fps=60)

    def run(self):

        # init scene
        self.scene.activate()

        # # init game loop
        self.game_loop.init(screen=self.screen)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
