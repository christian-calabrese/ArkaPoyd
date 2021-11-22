from random import randrange

import pygame

import Settings


class GameView:
    def __init__(self, model, screen):
        pygame.font.init()
        self.__start_font = pygame.font.SysFont('Nunito', 24)
        self.__model = model
        self.__screen = screen
        self.__screen.fill(Settings.BG_COLOR)
        self.__real_bricks = []
        self.__real_bar = pygame.Rect(
            self.__model.bar.xpos - (self.__model.bar.width / 2),
            self.__model.bar.ypos - (self.__model.bar.height / 2),
            self.__model.bar.width, Settings.DEFAULT_BAR_HEIGHT
        )
        for brick in self.__model.bricks:  # Instantiate rects
            self.__real_bricks.append(pygame.Rect(
                brick.xpos, brick.ypos,
                brick.width, Settings.BRICK_HEIGHT
            )
            )

    def draw(self):
        # Refresh the screen
        self.__screen.fill(Settings.BG_COLOR)

        if (not self.__model.bullet.is_moving()):
            start_text = self.__start_font.render(
                "Press the space bar to start", True, (255, 0, 0)
            )
            start_rect = start_text.get_rect(center=self.__screen.get_rect().center)
            self.__screen.fill(Settings.BG_COLOR, start_rect)
            self.__screen.blit(start_text, start_rect)
        # Draw the bar
        self.__real_bar.centerx = self.__model.bar.xpos
        pygame.draw.rect(self.__screen, Settings.BAR_COLOR, self.__real_bar, 0)

        # Draw the bullet
        real_bullet = pygame.draw.circle(
            self.__screen, (0, 255, 255),
            self.__model.bullet.pos, Settings.BALL_RADIUS
        )

        # Draw the bricks
        for i in range(len(self.__model.bricks)):  # Draw rects
            brick = self.__model.bricks[i]
            real_brick = self.__real_bricks[i]
            if (brick.active):
                pygame.draw.rect(self.__screen, brick.color, real_brick, 1)
