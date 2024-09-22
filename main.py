import numpy as np
import pygame
from enum import Enum

from gameStates import start, menu, running, paused
from gameStates import game_state_manager as gsm
from gameStates.game_state_manager import State
import settings


pygame.init()
screen = pygame.display.set_mode(settings.RES, pygame.RESIZABLE)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


# Set start background
# Set up fonts
FONT_SIZE_TITLE = 100
FONT_SIZE_TEXT = 40
CREDIT_TEXT = 30
title_font = pygame.font.Font(None, FONT_SIZE_TITLE)
text_font = pygame.font.Font(None, FONT_SIZE_TEXT)
credit_font = pygame.font.Font(None, CREDIT_TEXT)


def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)


# Background fill
screen.fill((34, 52, 90))

# Display title
display_text(screen, "GAME OF LIFE", title_font, "white", (settings.WIDTH // 2, settings.HEIGHT // 4))

# Display credits
display_text(screen, "Created by", text_font, (83, 107, 148), (settings.WIDTH // 2, settings.HEIGHT - 60))
display_text(screen, "Ben Sanders-Wyatt", credit_font, (83, 107, 148), (settings.WIDTH // 2, settings.HEIGHT - 30))

# Update the screen
pygame.display.flip()

current_map = np.random.randint(2, size=(settings.H, settings.W))


# GAME LOOP
while gsm.get_game_state() != State.Quit:

    # EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gsm.set_game_state(State.Quit)

        match gsm.get_game_state():
            case State.Start:
                start.event(event)

            case State.Menu:
                menu.event(event)

            case State.Running:
                running.event(event)

            case State.Paused:
                paused.event(event)

    # UPDATE HANDLER
    match gsm.get_game_state():
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
