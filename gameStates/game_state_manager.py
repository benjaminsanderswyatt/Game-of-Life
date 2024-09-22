from enum import Enum


class State(Enum):
    Start = 0
    Menu = 1
    Running = 2
    Paused = 3
    Quit = 4


game_state = State.Start


def get_game_state():
    return game_state


def set_game_state(new_state):
    global game_state
    game_state = new_state
