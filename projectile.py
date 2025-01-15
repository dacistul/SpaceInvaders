import pygame
from pygame import Vector2
import Settings
from SpriteLib import ScaledSprite

explosion_fx = pygame.mixer.Sound("assets/sounds/sfx/explosion.wav")
explosion_fx.set_volume(Settings.VOLUME_EXPLOSION)
laser_fx = pygame.mixer.Sound("assets/sounds/sfx/blaster.mp3")
laser_fx.set_volume(Settings.VOLUME_LASER)

class Projectile(ScaledSprite):
	def __init__(self, x, y, scale):
		super().__init__(scale,pygame.image.load("assets/textures/projectile.png"))
		self.rect.bottom = y
		self.rect.centerx = x

		laser_fx.play()

	def update(self, enemy_group):
		self.rect.y -= Settings.SPEED_PROJECTILE
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, enemy_group, True):
			self.kill()
			explosion_fx.play()
