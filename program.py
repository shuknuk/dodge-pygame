# Import module - pygame
import pygame

# Import pygame.locals | Detect hardware input from user:
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen object | Determined by width+height of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Keep loop running, variable config:
running = True

# Script of loop:
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Detect input of key from user
        if event.type == KEYDOWN:
            # If key having to be esc, suspend program:
            if event.key == K_ESCAPE:
                running = False

        # Manual suspending program using X-button
        elif event.type == QUIT:
            running = False

# Screen with white (imma prob. change it to another color later, idk)
screen.fill((255, 255, 255))

# Surface length and width
surf = pygame.Surface((50, 50))

# Surface be separate from background
surf.fill((0, 0, 0))
rect = surf.get_rect()

# The following commands below this will use .blit() and .flip()
# Note, .blit() stands for Block Transfer
# This line says: "Draw surf onto screen at center"
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()
