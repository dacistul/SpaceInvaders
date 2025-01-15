import pygame
import Settings

pygame.mixer.init()
pygame.init()

from Ship import Ship
from HealthBar import HealthBar
from Enemy import Enemy

screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

NAME = "Galaga"
pygame.display.set_caption(NAME)

clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load("assets/sounds/music/hyper.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

bg_img = pygame.image.load("assets/textures/background.png")
bg = pygame.transform.scale(bg_img, (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
bg_pos = 0


def draw_bg():
	global bg_pos
	screen.blit(bg, (0, bg_pos))
	screen.blit(bg, (0, bg_pos - Settings.SCREEN_HEIGHT))
	if bg_pos == Settings.SCREEN_HEIGHT:
		bg_pos = 0
	bg_pos += 1

health = 3

ship_group = pygame.sprite.Group()
ship = Ship(int(Settings.SCREEN_WIDTH / 2), 90/100*Settings.SCREEN_HEIGHT)
ship_group.add(ship)


ui_group = pygame.sprite.Group()

healthBar = HealthBar()
ui_group.add(healthBar)

proj_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

ROWSENEMY = 2
COLUMNSENEMY = 12

for i in range(0, ROWSENEMY):
	for j in range(0, COLUMNSENEMY):
		enemy = Enemy(-0.9 * Settings.SCREEN_WIDTH + 1.8*Settings.SCREEN_WIDTH/(COLUMNSENEMY - 1) * j, 0.12 * Settings.SCREEN_HEIGHT * (i + 1), 3)
		enemy_group.add(enemy)

score = 0
ENEMYVALUE = 5
initNoEnemies = len(enemy_group.sprites())

font = pygame.font.SysFont("Arial", 32)

#game loop
run = True
while run:
	clock.tick(FPS)
	draw_bg()

	ship.update(proj_group, enemy_group)
	ship_group.draw(screen)

	enemy_group.update()
	enemy_group.draw(screen)

	proj_group.update(enemy_group)
	proj_group.draw(screen)

	ui_group.draw(screen)


	score = (initNoEnemies - len(enemy_group.sprites())) * ENEMYVALUE

	healthBar.setHealth(health)

	if ship.ok != 1 and health > 0:
		health-=1
		ship = Ship(int(Settings.SCREEN_WIDTH / 2), 90/100*Settings.SCREEN_HEIGHT)
		ship_group.add(ship)

	# if ship.ok == 1:
	# 	txtsurf = font.render("Score: " + str(score), True, (255, 255, 255))
	# 	screen.blit(txtsurf, (0, 0))
	# else:
	# 	txtsurf = font.render("Dead", True, (255, 0, 0))
	# 	screen.blit(txtsurf, (0, 0))

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
