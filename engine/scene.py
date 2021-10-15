from typing import List
from .game_object import GameObject


class Scene:

    __active_scene__ = None

    def __init__(self, game_objects: List[GameObject], width=600, height=600):

        self.__new_objects__ = game_objects  # set(game_objects)
        self.__active_objects__ = list()  # set()
        self.__deleted_objects__ = list()  # []
        self.__width__ = width
        self.__height__ = height

    @property
    def height(self):
        return self.__height__

    @property
    def width(self):
        return self.__width__

    @classmethod
    def get_active_scene(cls) -> "Scene":
        return cls.__active_scene__

    @classmethod
    def add_to_active_scene(cls, game_object):
        try:
            cls.get_active_scene().load_game_object(game_object)
        except AttributeError:
            print("No active scene available.")

    def load_game_object(self, game_object):
        self.__new_objects__.append(game_object)
        # self.__new_objects__ = sorted(self.__new_objects__, key=lambda game_object: game_object.order)

    def remove_game_object(self, game_object):
        self.__active_objects__.remove(game_object)

    def activate(self):
        Scene.__active_scene__ = self

    @classmethod
    def get_game_objects(cls):
        return cls.get_active_scene().get_active_game_objects()

    def get_active_game_objects(self):
        return self.__active_objects__

    def update_scene(self):
        while True:
            try:
                item = self.__new_objects__.pop()
                self.__active_objects__.append(item)
                self.__active_objects__ = sorted(
                    self.__active_objects__, key=lambda game_object: game_object.order
                )
            except IndexError:
                break

        while True:
            try:
                item = self.__deleted_objects__.pop()
                self.__active_objects__.remove(item)
            except IndexError:
                break

    @classmethod
    def find_game_object(cls, name):
        """Searches a game object by name"""
        game_objects = cls.get_game_objects()

        for game_object in game_objects:
            if game_object.name == name:
                return game_object

        return None
