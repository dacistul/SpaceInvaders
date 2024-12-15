import random
import pygame

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self._scale = 1
		self.health = health
		self.image = pygame.image.load("assets/textures/enemies/enemy1.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.mask = pygame.mask.from_surface(self.image)
		self.setScale(2.2)
	
	def setScale(self, scale):
		new_width = self.rect.w * scale / self._scale
		new_height = self.rect.h * scale / self._scale
		self.rect = pygame.Rect((self.rect.x + (self.rect.w - new_width) / 2,
						self.rect.y + (self.rect.h - new_height) / 2,
						self.rect.w * scale / self._scale,
						self.rect.h * scale / self._scale))
		self._scale = scale
		self.image = pygame.transform.scale_by(self.image, self._scale)
	
	def update(self):
		pass
