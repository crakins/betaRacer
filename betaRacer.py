import pygame, sys
from pygame.locals import *
import time
from Models.Enemy import Enemy
from Models.Player import Player

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

# Oscar challenge: change background to AnimatedStreet.png
# pygame.image.load("resources/images/Enemy.png")

DOVE_ROAD = pygame.image.load("resources/images/Animatedstreet.png")

# Screen information
SCREEN_WIDTH =  400
SCREEN_HEIGHT = 600
SPEED = 5

# Create background
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.blit(DOVE_ROAD,[0, 0])
pygame.display.set_caption("Road Racer BETA")

# Setup Sprites
E1 = Enemy()
P1 = Player()

# Create Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Add a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    # Cycle through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Background
    DISPLAYSURF.blit(DOVE_ROAD,[0, 0])
    
    # Moves and re-draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # To be run if a collission occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # P1.update()
    # E1.move()
    
    
    # P1.draw(DISPLAYSURF)
    # E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
