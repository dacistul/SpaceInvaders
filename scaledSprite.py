import pygame

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
