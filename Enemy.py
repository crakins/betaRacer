import pygame
from pygame.locals import *
import random

# Screen information
SCREEN_WIDTH =  400
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("resources/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)