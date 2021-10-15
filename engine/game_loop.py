import sys
import pygame as pg

from .scene import Scene


class GameLoop:
    def __init__(self, limit_fps=60):
        self.limit_fps = limit_fps
        self.clock = pg.time.Clock()

    def init(self, screen=None):
        self.screen = screen
        self.__start_game_loop__()

    def __start_game_loop__(self):

        game_objects = Scene.get_game_objects()

        for game_object in game_objects:
            game_object.start()

        while True:
            self.screen.fill((0, 0, 0))

            if pg.event.get(eventtype=[pg.QUIT]):
                # if event.type == pg.QUIT:
                sys.exit(0)

            events = pg.event.get()

            # tick the clock
            dt = self.clock.tick(self.limit_fps)

            # update scene objects (clean resources)
            Scene.get_active_scene().update_scene()

            # get all objects in the active scene
            game_objects = Scene.get_game_objects()

            for game_object in game_objects:

                # start game objects
                if not game_object.started:
                    game_object.start()

                # destroy game objects
                if game_object.destroyed:
                    Scene.get_active_scene().remove_game_object(game_object)

                # handle input
                game_object.input(events)  # pass events

                # handle update and fixed update?...
                game_object.update()

                game_object.fixed_update(dt)

                # handle render
                game_object.render(self.screen)

            pg.display.update()
