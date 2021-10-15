# Game engine with Python

This is a basic implementation of a Game engine using Python and Pygame for rendering
2D graphics. It is heavily based on the videos from the youtube channel 
[StackOrient Technologies](https://www.youtube.com/watch?v=aXweZxNEEwk).


## Structure

There are 3 main components composing the game engine:

- Game Object
- Game Loop
- Sceme

### Game Object

The Game object is an object which holds properties and methods for 2D transformations.

### Scene

The Scene is an object which groups and manages Game objects.

### Game Loop

The Game Loop is an object which detects the current active Scene and iterates over all
the game objects in the scene, allowing the call of different methods (input, update, render).

Basically, the game loop ensures that each game object in the current active scene is updated
and rendered to the screen.

## Implementation example

```py
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
```

## License

Please feel free to use it as you wish! :)