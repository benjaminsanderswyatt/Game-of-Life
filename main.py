import numpy as np
import pygame
from enum import Enum

from gameStates import start, running, paused
import settings


pygame.init()
screen = pygame.display.set_mode(settings.RES)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


class State(Enum):
    Start = 0
    Running = 1
    Paused = 2
    Quit = 3


gameState = State.Running

current_map = np.random.randint(2, size=(settings.H, settings.W))


while gameState != State.Quit:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = State.Quit

    match gameState:
        case State.Start:
            print("start")

        case State.Running:

            temp = running.main_running(screen, current_map)

            current_map = np.copy(temp)

        case State.Paused:
            print("Paused")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(settings.FPS)

pygame.quit()
