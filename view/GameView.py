import pygame
import Settings
from random import randrange

class GameView:
    def __init__(self, model, screen):
        pygame.font.init()
        self.__model = model
        self.__screen = screen
        self.__screen.fill(Settings.BG_COLOR)
        self.__real_bricks = []
        self.__real_bar = pygame.Rect(self.__model.bar.xpos - (self.__model.bar.width / 2), self.__model.bar.ypos - (self.__model.bar.height / 2), self.__model.bar.width, Settings.DEFAULT_BAR_HEIGHT)
        for brick in self.__model.bricks: # Instantiate rects
            self.__real_bricks.append(pygame.Rect(brick.xpos, brick.ypos, brick.width, Settings.BRICK_HEIGHT))


    def draw(self):
        self.__screen.fill(Settings.BG_COLOR)
        # Draw the bar
        self.__real_bar.centerx = self.__model.bar.xpos
        pygame.draw.rect(self.__screen, Settings.BAR_COLOR, self.__real_bar, 0)

        # Draw the bullet
        real_bullet = pygame.draw.circle(self.__screen, (255, 0, 0), self.__model.bullet.pos, Settings.BALL_RADIUS)

        # Draw the bricks
        for i in range(len(self.__model.bricks)): # Instantiate rects
            brick = self.__model.bricks[i]
            real_brick = self.__real_bricks[i]
            pygame.draw.circle(self.__screen, (255, 0, 0), (real_brick.x, real_brick.y), 1)
            pygame.draw.circle(self.__screen, (0, 255, 0), (brick.xpos, brick.ypos), 1)
            if(brick.active):
                pygame.draw.rect(self.__screen, brick.color, real_brick, 1)

