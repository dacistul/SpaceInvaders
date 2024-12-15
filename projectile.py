import pygame

pygame.mixer.init()

explosion_fx = pygame.mixer.Sound("assets/sounds/sfx/explosion.wav")
explosion_fx.set_volume(0.2)

class Projectile(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		self._scale = 1
		self.image = pygame.image.load("assets/textures/projectile.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.mask = pygame.mask.from_surface(self.image)
		self.setScale(scale)
	
	def setScale(self, scale):
		new_width = self.rect.w * scale / self._scale
		new_height = self.rect.h * scale / self._scale
		self.rect = pygame.Rect((self.rect.x + (self.rect.w - new_width) / 2,
						self.rect.y + (self.rect.h - new_height) / 2,
						self.rect.w * scale / self._scale,
						self.rect.h * scale / self._scale))
		self._scale = scale
		self.image = pygame.transform.scale_by(self.image, self._scale)

	def update(self, speed, enemy_group):
		self.rect.y -= speed
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, enemy_group, True):
			self.kill()
			explosion_fx.play()
