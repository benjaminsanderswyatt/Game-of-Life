import pygame
import numpy as np

RES = WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
W, H = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 10

current_state = np.random.randint(2, size=(H, W))
next_state = np.zeros_like(current_state)



def check_cell_surroundings(current_state, x, y):
    count = 0

    # Check the surrounding cells
    for i in range(max(0, y - 1), min(H, y + 2)):
        for j in range(max(0, x - 1), min(W, x + 2)):
            if current_state[i][j]:
                count += 1

    # If the cell was originally alive subtract itself from the count
    if current_state[y][x]:
        count -= 1

    # Apply the Rules
    if current_state[y][x]:  # If the cell is alive
        if count == 2 or count == 3:
            return 1  # Cell stays alive
        return 0  # Cell dies
    else:  # If the cell is dead
        if count == 3:
            return 1  # Cell becomes alive
        return 0  # Cell stays dead




pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light gray")

    # RENDER GAME HERE
    # Draw grid
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, "black", (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, "black", (0, y), (WIDTH, y))

    # Draw cells

    for x in range(0, W):
        for y in range(0, H):
            if current_state[y][x]:
                # Draw the rectangle for a live cell
                pygame.draw.rect(screen, "black", (x * CELL_SIZE + 2, y * CELL_SIZE + 2, CELL_SIZE - 2, CELL_SIZE - 2))

            # Update the next state based on the surroundings
            next_state[y][x] = check_cell_surroundings(current_state, x, y)

    # Copy the next state to the current state for the next iteration
    current_state = np.copy(next_state)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()