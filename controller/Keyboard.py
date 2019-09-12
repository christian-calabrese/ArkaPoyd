import pygame
from model.Game import GameModel

class KeyboardController:

    def __init__(self, game: GameModel):
        self.game_model = game
        self.__counter = 0

    def events_handling(self, running):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.__counter > 0:
                    self.game_model.command_bar(-1)
                elif event.key == pygame.K_RIGHT and self.__counter > 0:
                    self.game_model.command_bar(1)
                elif event.key == pygame.K_ESCAPE:
                    running = pygame.quit()
                elif event.key == pygame.K_SPACE and self.__counter == 0:
                        self.__counter = 1
                        self.game_model.bullet.first_bump()
                break

        return running
