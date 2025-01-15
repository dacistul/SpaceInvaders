import pygame
import sys
from SpriteLib import AtlasSprite

class HealthBar(AtlasSprite):
    def __init__(self):
        super().__init__(1,4,pygame.image.load("assets/textures/health.png"),5)
        self.setHealth(3)


    def setHealth(self, health):
        self.selectSprite(0,health)
