# Main point of creating a simple python program.

# 1. First, to import the pygame library
# This code will also initialize the pygame library

import pygame
pygame.init()

# Size of the window
screen = pygame.display.set_mode([500, 500])

# Having the game be running until suspended by user:
running = True
while running:

    # Making value X-button = close_window_button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gray background! | Fill background with a gray color. 
    # Gray color has number 200. 
    screen.fill((200, 200, 200))

    # Blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Script complete! If having to quit the program:
pygame.quit()