from socket import gaierror
import pygame, sys
from pygame.locals import *
import time
from Models.Enemy import Enemy
from Models.Player import Player
import globals

# Initialize program
pygame.init()
globals.init()

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
# Hint: pygame.image.load("resources/images/Enemy.png")

DOVE_ROAD = pygame.image.load("resources/images/Animatedstreet.png")

# Screen information
SCREEN_WIDTH =  400
SCREEN_HEIGHT = 600

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create background
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('./resources/images/AnimatedStreet.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# DISPLAYSURF.blit(DOVE_ROAD,[0, 0]) # used for static background
pygame.display.set_caption("Road Racer BETA")

# Setup Sprites
E1 = Enemy()
P1 = Player()

# Setup Background
back_ground = Background()

# Create Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Add a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Setup background music
pygame.mixer.music.load('./resources/sounds/background.wav')

# Play background music
pygame.mixer.music.play(-1)

# Game Loop
while True:
    # Cycle through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            globals.SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Background
    back_ground.update()
    back_ground.render()
    # DISPLAYSURF.blit(DOVE_ROAD,[0, 0]) # static background
    score_text = "Score: " + str(globals.SCORE)
    scores = font_small.render(str(score_text), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and re-draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if a collission occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('./resources/sounds/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
