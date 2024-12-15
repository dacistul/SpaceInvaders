import pygame
from projectile import Projectile

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 720

laser_fx = pygame.mixer.Sound("assets/sounds/sfx/blaster.mp3")
laser_fx.set_volume(0.25)

class Ship(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self._scale = 1
		self.image = pygame.image.load("assets/textures/spaceship.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.mask = pygame.mask.from_surface(self.image)
		self.health_start = health
		self.health_remaining = health
		self.lastProj_timestamp = pygame.time.get_ticks()
		self.ok = 1

	def setScale(self, scale):
		new_width = self.rect.w * scale / self._scale
		new_height = self.rect.h * scale / self._scale
		self.rect = pygame.Rect((self.rect.x + (self.rect.w - new_width) / 2,
						self.rect.y + (self.rect.h - new_height) / 2,
						self.rect.w * scale / self._scale,
						self.rect.h * scale / self._scale))
		self._scale = scale
		self.image = pygame.transform.scale_by(self.image, self._scale)

	def update(self, proj_group, enemy_group, speed, cooldown):
		if self.ok == 1:
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT] and self.rect.left > 0:
				self.rect.x -= speed
			if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
				self.rect.x += speed
			if key[pygame.K_UP] and self.rect.top > 0:
				self.rect.y -= speed
			if key[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
				self.rect.y += speed
			
			timestamp = pygame.time.get_ticks()
			if key[pygame.K_SPACE] and timestamp - self.lastProj_timestamp > cooldown:
				proj = Projectile(self.rect.centerx, self.rect.top, self._scale)
				proj_group.add(proj)
				laser_fx.play()
				self.lastProj_timestamp = timestamp
		
		if pygame.sprite.spritecollide(self, enemy_group, True):
			self.kill()
			self.ok = 0
		