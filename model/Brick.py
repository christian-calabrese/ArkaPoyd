from typing import Dict, Tuple
from random import randrange
import Settings


class Brick:
    def __init__(self, position: Dict):
        self.__pos = position
        self.__width = Settings.BRICK_WIDTH
        self.__height = Settings.BRICK_HEIGHT
        self.__color = (
            randrange(100, 255),
            randrange(100, 255),
            randrange(100, 255)
        )
        self.__active = True

    def explode(self):
        self.__active = False

    @property
    def xpos(self) -> int:
        return self.__pos["x"]

    @property
    def ypos(self) -> int:
        return self.__pos["y"]

    @property
    def color(self) -> Tuple:
        return self.__color

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def active(self) -> bool:
        return self.__active
