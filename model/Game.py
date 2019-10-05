import Settings
from model.Brick import Brick
from model.Status import Status
from model.Bar import Bar
from model.Bullet import Bullet
from typing import List
import math


class GameModel:
    def __init__(self):
        self.__level = 1
        self.__bricks = self.__generateBricks(
            Settings.ROWS_LEVEL[self.__level - 1]
        )
        self.__bar = Bar()
        bullet_start = {
            "x": self.__bar.xpos - (Settings.BALL_RADIUS / 2),
            "y": self.__bar.ypos - Settings.BALL_RADIUS
        }
        self.__bullet = Bullet(bullet_start)
        self.__score = 0
        self.__running = True

    # Generate and return a list of bricks with the right coordinates
    def __generateBricks(self, qnt: int) -> List:
        createdbricks = []
        bricksperrow = int(Settings.WIDTH / Settings.BRICK_WIDTH)

        for i in range(qnt):
            for j in range(bricksperrow):
                xpos = j * Settings.BRICK_WIDTH
                ypos = i * Settings.BRICK_HEIGHT
                createdbricks.append(Brick({"x": xpos, "y": ypos}))
        return createdbricks

    def step(self) -> int:
        self.__bar.move()
        if self.__bullet.move():
            # Check if the bullet hits the bar
            if rect_circ_collide(
                self.__bar.xpos, self.__bar.ypos,
                self.__bar.width, self.__bar.height,
                self.__bullet.pos[0], self.__bullet.pos[1],
                self.__bullet.radius
            ):
                self.__bullet.hit(self.__bar.xpos, self.__bar.ypos, True)
            # Check if any of the bricks is hit by the bullet
            for brick in self.__bricks:
                if brick.active and
                rect_circ_collide(
                    brick.xpos, brick.ypos,
                    brick.width, brick.height,
                    self.__bullet.pos[0], self.__bullet.pos[1],
                    self.__bullet.radius
                ):
                    self.__bullet.hit(brick.xpos, brick.ypos, False)
                    self.__score += 1
                    brick.explode()
                    # If there are bricks left
                    if not self.__bricks:
                        return Status.NEUTRAL
                    else:
                        return Status.WON
        else:
            self.__running = False
            return Status.LOST

    def command_bar(self, dir: int):
        self.__bar.xdir = dir

    @property
    def bricks(self) -> List:
        return self.__bricks

    @property
    def bar(self) -> Bar:
        return self.__bar

    @property
    def bullet(self) -> Bullet:
        return self.__bullet

    @property
    def running(self) -> bool:
        return self.__running

    @property
    def score(self) -> int:
        return self.__score


def rect_circ_collide(r_x, r_y, r_w, r_h, c_x, c_y, c_r):
    dist = math.sqrt((r_x - c_x) * (r_x - c_x) + (r_y - c_y) * (r_y - c_y))
    return dist <= c_r + r_w

    # For rectangles (it doesn't really work)
    # return c_x < r_x + c_r and c_x + r_w > r_x and c_y < r_y + c_r and r_h + c_y > r_y
