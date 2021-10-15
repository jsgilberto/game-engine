from abc import ABC

# from engine.scene import Scene
from typing import List, Text


class Transform:
    def __init__(self, x=0, y=0, width=0, height=0, scale_x=1, scale_y=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y

    @property
    def center(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2

        return x, y

    def change_position(self, x, y):
        self.x = x or self.x
        self.y = y or self.y

    def change_dimension(self, width, height):
        self.width = width or self.width
        self.height = height or self.height

    def change_scale(self, sx, sy):
        self.scale_x = sx + self.scale_x
        self.scale_y = sy + self.scale_y


class AbstractGameObject(ABC):
    def __init__(
        self,
        transform: Transform,
        tags: List[str] = None,
        name: Text = None,
        order: int = None,
    ):

        self.__transform__ = transform or Transform()

        self.__tags__ = tags

        self.__name__ = name

        self.__order__ = order or 1

    @property
    def order(self):
        return self.__order__

    @property
    def transform(self):
        return self.__transform__

    @property
    def tags(self):
        return self.__tags__

    @property
    def name(self):
        return self.__name__

    def input(self, events):
        pass

    def update(self):
        pass

    def fixed_update(self, dt):
        pass

    def render(self, screen):
        pass


class GameObject(AbstractGameObject):
    """Class used to represent Players, props, etc."""

    def __init__(
        self,
        transform: Transform,
        tags: List[str] = None,
        name: Text = None,
        order: int = None,
    ):
        super().__init__(transform=transform, tags=tags, name=name, order=order)

        self.init()
        self.started = False
        self.destroyed = False

    def init(self):
        pass

    def start(self):
        self.started = True

    def destroy(self):
        self.destroyed = True

    def get_collision(self, game_objects: List["GameObject"]):

        for game_object in game_objects:
            if game_object is self:
                continue

            if (
                game_object.__is_in_horizontal__(self.transform.x)
                or game_object.__is_in_horizontal__(
                    self.transform.x + self.transform.width
                )
            ) and (
                game_object.__is_in_vertical__(self.transform.y)
                or game_object.__is_in_vertical__(
                    self.transform.y + self.transform.height
                )
            ):
                return game_object
        return None

    def __is_in_horizontal__(self, x):
        return (x > self.transform.x) and (x < self.transform.x + self.transform.width)

    def __is_in_vertical__(self, y):
        return (y > self.transform.y) and (y < self.transform.y + self.transform.height)

    def __str__(self):
        return f"Name: '{self.name}' - Tags: {self.tags}"


class SelectableMixin:

    __hovered__ = None
    __selected__ = None

    def __is_hovered__(self, x, y):
        return (
            (x > self.transform.x)
            and (x < self.transform.x + self.transform.width)
            and (y > self.transform.y)
            and (y < self.transform.y + self.transform.height)
        )

    @classmethod
    def set_selected(cls, game_object):
        cls.__selected__ = game_object

    @classmethod
    def get_selected(cls):
        return cls.__selected__
