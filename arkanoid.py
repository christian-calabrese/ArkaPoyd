import sys
import pygame
from controller.Keyboard import KeyboardController
from model.Game import GameModel
from view.GameView import GameView
import Settings


def main():
    pygame.init()
    pygame.display.set_caption("Arkanoid")
    screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

    fps = 120
    clock = pygame.time.Clock()

    model = GameModel()
    controller = KeyboardController(model)
    view = GameView(model, screen)

    while model.running:
        controller.events_handling(model.running)

        model.step()

        view.draw()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)

    # Push scores to a DynamoDB through AWS Lambda
    # leaderboard.push(model.score)

if __name__ == "__main__":
    main()
