import pygame

RES = WIDTH, HEIGHT = 800, 600
TILE = 50
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

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
    screen.fill(pygame.Color('grey77'))

    # RENDER YOUR GAME HERE
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, pygame.Color('black'), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, pygame.Color('black'), (0, y), (WIDTH, y))





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()