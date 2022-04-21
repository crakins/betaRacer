import pygame, sys
from pygame.locals import *
import random
import Enemy

# Initialize program
pygame.init()

# Assign FPS value
FPS = 60
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH =  400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill (WHITE)
pygame.display.set_caption("Road Racer beta")

# Create class objects
E1 = Enemy.Enemy()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    E1.move()

    DISPLAYSURF.fill(WHITE)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
