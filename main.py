import numpy as np
import pygame
from enum import Enum

from gameStates import start, menu, running, paused
import settings


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


class State(Enum):
    Start = 0
    Menu = 1
    Running = 2
    Paused = 3
    Quit = 4


gameState = State.Running

current_map = np.random.randint(2, size=(settings.H, settings.W))


# GAME LOOP
while gameState != State.Quit:

    # EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = State.Quit
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.w, event.h
            settings.WIDTH, settings.HEIGHT = event.w, event.h

        match gameState:
            case State.Start:
                start.event(event)

            case State.Menu:
                menu.event(event)

            case State.Running:
                running.event(event)

            case State.Paused:
                paused.event(event)

    # UPDATE HANDLER
    match gameState:
        case State.Start:
            start.main_start(screen)
            start.render(screen)

        case State.Menu:
            menu.main_menu(screen)

        case State.Running:

            temp = running.main_running(screen, current_map)

            current_map = np.copy(temp)

        case State.Paused:
            paused.main_paused()

    # flip() the display to put your work on screen
    pygame.display.flip()
    # pygame.display.update()

    clock.tick(settings.FPS)

pygame.quit()
