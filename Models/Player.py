import pygame
from pygame.locals import *

# Screen information
SCREEN_WIDTH =  400
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # up
        if self.rect.top > 10:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        # down 
        if self.rect.bottom < SCREEN_HEIGHT-20:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        # left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        #right
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)