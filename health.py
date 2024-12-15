import pygame
import sys


pygame.init()

class ScaledSprite(pygame.sprite.Sprite):
    def __init__(self, scale, image,position=pygame.Vector2()):
        super().__init__()
        self._scale = 1
        self.image = image
        self.rect = pygame.Rect((0,0,image.get_width(),image.get_height()))
        self.setPosition(position)
        self.setScale(scale)

    def setPosition(self, position):
        self.rect.x=position.x
        self.rect.y=position.y

    def setScale(self, scale):
        self._scale = scale

        self.rect = pygame.Rect((self.rect.x,self.rect.y,self.rect.w*scale/self._scale,
                          self.rect.h*scale/self._scale))
        self.image = pygame.transform.scale_by(self.image, self._scale)

class AtlasSprite(ScaledSprite):
    def __init__(self, spritesX, spritesY, atlas, scale):
        self._atlas = atlas
        self._spriteWidth = int(atlas.get_width()/spritesX)
        self._spriteHeight = int(atlas.get_height()/spritesY)
        super().__init__(scale, pygame.Surface((self._spriteWidth, self._spriteHeight)))

    def selectSprite(self, xIndex=0, yIndex=0):
        self.image = pygame.transform.scale_by(self._atlas.subsurface((self._spriteWidth*xIndex,self._spriteHeight*yIndex,self._spriteWidth,self._spriteHeight)), self._scale)

class HealthBar(AtlasSprite):
    def __init__(self):
        super().__init__(1,3,pygame.image.load("assets/textures/health.png"),5)
        self.setHealth(2)


    def setHealth(self, health):
        self.selectSprite(0,health-1)



display = pygame.display.set_mode((640, 480))
hb = HealthBar()

rootGroup = pygame.sprite.Group()
uiGroup = pygame.sprite.Group()
rootGroup.add(hb)
health=1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    health = health + 1
    if health > 3:
        health = 1
    hb.setHealth(health)

    rootGroup.draw(display)
    pygame.display.update()
    pygame.time.delay(1000)
    