import pygame
import sys
pygame.init()

# set screen size and also name of screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kokiri Shop Simulator")

# fps cap using clock and tick speed
clock = pygame.time.Clock()

# game variables
player = pygame.rect()

# true toggle boolean for loop
running = True

# create loop so pygame runs as screen as long as needed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            print(event.key)

    # Repaint screen with green 60 times a second for 60fps
    screen.fill((85, 150, 70))
    pygame.display.flip()
    clock.tick(60)
    #everything after this!!!


pygame.quit()
sys.exit()
