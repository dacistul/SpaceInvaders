import pygame
import Settings
from pygame import Vector2
from Projectile import Projectile
from SpriteLib import ScaledSprite


class Ship(ScaledSprite):
	def __init__(self, x, y):
		super().__init__(1,pygame.image.load("assets/textures/spaceship.png"),Vector2(x,y))
		self.lastProj_timestamp = pygame.time.get_ticks()
		self.ok = 1

	def update(self, proj_group, enemy_group):
		if self.ok == 1:
			key = pygame.key.get_pressed()
			move = Vector2(	(-Settings.SPEED_SHIP if key[pygame.K_LEFT] and self.rect.left > 0 else 0) + (Settings.SPEED_SHIP if key[pygame.K_RIGHT] and self.rect.right  < Settings.SCREEN_WIDTH  else 0),
							(-Settings.SPEED_SHIP if key[pygame.K_UP]   and self.rect.top  > 0 else 0) + (Settings.SPEED_SHIP if key[pygame.K_DOWN]  and self.rect.bottom < Settings.SCREEN_HEIGHT else 0))

			self.addPosition(move)

			timestamp = pygame.time.get_ticks()
			if key[pygame.K_SPACE] and timestamp - self.lastProj_timestamp > Settings.PROJECTILE_COOLDOWN:
				proj = Projectile(self.rect.centerx, self.rect.top, self._scale)
				proj_group.add(proj)
				self.lastProj_timestamp = timestamp
		
		if pygame.sprite.spritecollide(self, enemy_group, True):
			self.kill()
			self.ok = 0
