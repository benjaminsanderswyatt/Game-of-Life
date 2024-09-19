import numpy as np
import pygame
import ui.buttons
import settings

my_button = ui.buttons.Button('Click Me!', "red", "yellow", "blue", "Orange", 10, 10, 200, 100, True)


def render(screen):
    my_button.draw(screen)



def event(event):
    if my_button.check_clicked():
        print("do something")



def main_start(screen):
    # TODO: display grid
    return 0