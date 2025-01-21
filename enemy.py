import random
import pygame
import Settings
from pygame import Vector2
from SpriteLib import ScaledSprite

directions = [Vector2( 1, 0),
			  Vector2( 0,1),
			  Vector2(-1, 0),
			  Vector2( 0, 1)]

class Enemy(ScaledSprite):
	def __init__(self, x, y, health):
		super().__init__(2,pygame.image.load("assets/textures/enemies/enemy1.png"))
		self.health = health
		self.rect.center = Vector2(x, y)
		self.mask = pygame.mask.from_surface(self.image)

		self.direction = 0
		self.last_turn = Vector2(x,y)
	
	def update(self, level):
		if self.direction == 0 and self.rect.right > Settings.SCREEN_WIDTH-10:
			self.direction = 1
			self.last_turn = Vector2(self.rect.center)
		if self.direction == 1 and self.rect.top > self.last_turn.y + 0.06*Settings.SCREEN_HEIGHT:
			self.direction = 2
			self.last_turn = Vector2(self.rect.center)
		if self.direction == 2 and self.rect.left < 10:
			self.direction = 3
			self.last_turn = Vector2(self.rect.center)
		if self.direction == 3 and self.rect.top > self.last_turn.y + 0.06*Settings.SCREEN_HEIGHT:
			self.direction = 0
			self.last_turn = Vector2(self.rect.center)
		self.addPosition(directions[self.direction]*(1.0+(level/10)))


