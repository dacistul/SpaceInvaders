import pygame
from pygame import Vector2
from pygame.locals import *

class ScaledSprite(pygame.sprite.Sprite):
    def __init__(self, scale, image, position:Vector2 = Vector2()):
        super().__init__()
        self._scale = 1
        self.image = image
        self.rect = pygame.Rect((0,0,image.get_width(),image.get_height()))
        self.setPosition(position)
        self.setScale(scale)

    def setPosition(self, position:Vector2):
        self.rect.x=position.x
        self.rect.y=position.y
    def addPosition(self, position:Vector2):
        self.rect.x+=position.x
        self.rect.y+=position.y

    def setScale(self, scale):
        self.rect = pygame.Rect((self.rect.x,self.rect.y,self.rect.w*scale/self._scale,
                          self.rect.h*scale/self._scale))
        self.image = pygame.transform.scale_by(self.image, scale/self._scale)
        self.mask = pygame.mask.from_surface(self.image)
        self._scale = scale

class AtlasSprite(ScaledSprite):
    def __init__(self, spritesX, spritesY, atlas, scale):
        self._atlas = atlas
        self._spriteWidth = int(atlas.get_width()/spritesX)
        self._spriteHeight = int(atlas.get_height()/spritesY)
        super().__init__(scale, pygame.Surface((self._spriteWidth, self._spriteHeight)))

    def selectSprite(self, xIndex=0, yIndex=0):
        self.image = pygame.transform.scale_by(self._atlas.subsurface((self._spriteWidth*xIndex,self._spriteHeight*yIndex,self._spriteWidth,self._spriteHeight)), self._scale)

