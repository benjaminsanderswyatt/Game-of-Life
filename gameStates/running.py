import numpy as np
import pygame

import settings

# Calibrate settings
CELL_SIZE = settings.CELL_SIZE
CELL_MARGIN = settings.CELL_MARGIN
CELL_COLOR = settings.CELL_COLOR
BG_COLOR = settings.BG_COLOR

GRID_COLOR = settings.GRID_COLOR

W, H = settings.W, settings.H
FPS = settings.FPS


# Create a separate surface for the grid
grid_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
grid_surface.fill(BG_COLOR)  # Fill the background

# Draw the grid lines on the surface
for x in range(0, settings.WIDTH, CELL_SIZE):
    pygame.draw.line(grid_surface, GRID_COLOR, (x, 0), (x, settings.HEIGHT))
for y in range(0, settings.HEIGHT, CELL_SIZE):
    pygame.draw.line(grid_surface, GRID_COLOR, (0, y), (settings.WIDTH, y))


def check_cell_surroundings(current_map, x, y):
    count = 0
    rows, cols = current_map.shape

    # Check the surrounding cells
    for i in range(max(0, y - 1), min(settings.H, y + 2)):
        for j in range(max(0, x - 1), min(settings.W, x + 2)):
            # Wrap around using modulo
            ni = i % rows
            nj = j % cols
            if current_map[ni][nj]:
                count += 1

    # If the cell was originally alive subtract itself from the count
    if current_map[y][x]:
        count -= 1

    # Apply the Rules
    if current_map[y][x]:  # If the cell is alive
        if count == 2 or count == 3:
            return 1  # Cell stays alive
        return 0  # Cell dies
    else:  # If the cell is dead
        if count == 3:
            return 1  # Cell becomes alive
        return 0  # Cell stays dead


def main_running(screen, current_map):
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(grid_surface, (0, 0))

    next_map = np.copy(current_map)

    # Draw cells
    for x in range(0, W):
        for y in range(0, H):
            if current_map[y][x]:
                # Draw the rectangle for a live cell
                pygame.draw.rect(screen, CELL_COLOR, (x * CELL_SIZE + CELL_MARGIN, y * CELL_SIZE + CELL_MARGIN, CELL_SIZE - CELL_MARGIN, CELL_SIZE - CELL_MARGIN))

            # Update the next state based on the surroundings
            next_map[y][x] = check_cell_surroundings(current_map, x, y)

    return next_map

def event(event):
    return 0