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

# Define screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# That surface drawn on screen is now attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# Initialize pygame
pygame.init()

# Create screen object | Determined by width+height of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

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

# Fill the screen with black
screen.fill((0, 0, 0))

# Draw the player on the screen
screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Update the display
pygame.display.flip()