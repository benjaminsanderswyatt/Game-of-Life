import numpy as np
import pygame
import ui.buttons
import settings

my_button = ui.buttons.Button('Click Me!', "red", "yellow","Green", "blue", "Orange", 10, 10, 200, 100, True)


def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)


# Set start background
# Set up fonts
FONT_SIZE_TITLE = 100
FONT_SIZE_TEXT = 40
CREDIT_TEXT = 30
title_font = pygame.font.Font(None, FONT_SIZE_TITLE)
text_font = pygame.font.Font(None, FONT_SIZE_TEXT)
credit_font = pygame.font.Font(None, CREDIT_TEXT)


def render(screen):
    # Background fill
    screen.fill("dim gray")

    # Display title
    display_text(screen, "GAME OF LIFE", title_font, "white", (settings.WIDTH // 2, settings.HEIGHT // 4))

    # Display instructions
    display_text(screen, "Press Enter to Start", text_font, "light gray", (settings.WIDTH // 2, settings.HEIGHT // 2))
    display_text(screen, "Press Space to Pause", text_font, "light gray", (settings.WIDTH // 2, settings.HEIGHT // 2 + 50))

    # Display credits
    display_text(screen, "Created by", text_font, "gray", (settings.WIDTH // 2, settings.HEIGHT - 60))
    display_text(screen, "Ben Sanders-Wyatt", credit_font, "gray", (settings.WIDTH // 2, settings.HEIGHT - 30))

    my_button.draw(screen)



def event(event):
    if my_button.check_clicked():
        print("do something")



def main_start(screen):
    # TODO: display grid
    return 0