from typing import Dict

import Settings


class Bar():
    def __init__(self):
        self.__pos = {"x": (Settings.WIDTH / 2), "y": Settings.HEIGHT - 50}
        self.__xdir = 0
        self.__width = Settings.DEFAULT_BAR_LEN
        self.__height = Settings.DEFAULT_BAR_HEIGHT

    def move(self) -> int:
        increment = self.__xdir * 3
        if (
                (self.__pos["x"] - (self.__width / 2)) + increment > 0 and
                (self.__pos["x"] + (self.__width / 2)) + increment < Settings.WIDTH
        ):
            self.__pos["x"] = self.__pos["x"] + increment
            return increment
        return 0

    @property
    def xdir(self) -> int:
        return self.__xdir

    @xdir.setter
    def xdir(self, dir):
        self.__xdir = dir

    @property
    def xpos(self) -> int:
        return self.__pos["x"]

    @property
    def ypos(self) -> int:
        return self.__pos["y"]

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height
