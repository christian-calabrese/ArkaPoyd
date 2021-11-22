import math
from random import choice
from typing import Dict

import Settings
from model.Brick import Brick


class Bullet:
    def __init__(self, barpos: Dict):
        self.__pos = {
            "x": barpos["x"],
            "y": barpos["y"] - Settings.DEFAULT_BAR_HEIGHT - 5
        }
        self.__velocity = {"x": 0, "y": 0}
        self.__radius = Settings.BALL_RADIUS

    def hit(self, r_x, r_y, is_bar):
        mulvelx = 1 if self.__pos["x"] < r_x else -1
        mulvely = 1 if self.__pos["y"] < r_y else -1

        self.__velocity["x"] *= mulvelx
        if (is_bar):
            self.__velocity["y"] = -1
        else:
            self.__velocity["y"] *= mulvely

    def move(self) -> bool:  # Return None if the bullet touches the ground, return current position otherwise
        # Hit right/left border
        if (self.__pos["x"] + self.__radius) + self.__velocity["x"] >= Settings.WIDTH or \
                (self.__pos["x"] - self.__radius) + self.__velocity["x"] <= 0:
            self.__velocity["x"] *= -1  # Invert x velocity
        if (self.__pos["y"] - self.__radius <= 0):  # Hit the top border
            self.__velocity["y"] *= -1  # Invert y velocity

        if (self.__pos["y"] + self.__radius >= Settings.HEIGHT):
            return None
        self.__pos["x"] += self.__velocity["x"]
        self.__pos["y"] += self.__velocity["y"]
        return (int(self.__pos["x"]), int(self.__pos["y"]))

    def first_bump(self):
        self.__velocity["x"] = choice([-1, 1])
        self.__velocity["y"] = -1

    def __sign(self, x: int) -> int:
        return 1 - (x <= 0)

    def is_moving(self) -> bool:
        return self.__velocity["x"] != 0 or self.__velocity["y"] != 0

    @property
    def pos(self):
        return (int(self.__pos["x"]), int(self.__pos["y"]))

    @property
    def radius(self):
        return self.__radius
