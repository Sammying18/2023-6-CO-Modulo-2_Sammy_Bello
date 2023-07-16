from typing import Any
import pygame
from random import randint
from pygame.sprite import _Group, Sprite
from game.utils.constants import ENEMY_1,SHIP_WIDTH ,SHIP_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):    
    Y_POS = 20 
    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH ,SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,SCREEN_WIDTH)
        self.rect.y = self.Y_POS


    def update(self):
        pass
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)