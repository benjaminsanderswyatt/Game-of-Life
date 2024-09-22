import numpy as np
import pygame
import ui.buttons
import settings


btn_start = ui.buttons.Button('Start', 32, "white", "slate gray", (76, 78, 116), (76, 78, 116), (27, 22, 63),
                              settings.WIDTH // 2 - 200, settings.HEIGHT // 2, 400, 50, True)

btn_quit = ui.buttons.Button('Quit', 28, "white", "slate gray", (76, 78, 116), (76, 78, 116), (27, 22, 63),
                              settings.WIDTH // 2 - 150, settings.HEIGHT // 2 + 75, 300, 50, True)

def render(screen):
    btn_start.draw(screen)
    btn_quit.draw(screen)


def event(event):
    if btn_start.check_clicked():
        print("do something")


def main_start(screen):
    # TODO: display grid
    return 0