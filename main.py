import pygame
from ship import Ship
#from health import HealthBar
from enemy import Enemy

pygame.mixer.init()
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

NAME = "Galaga"
pygame.display.set_caption(NAME)

clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load("assets/sounds/music/hyper.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

bg_img = pygame.image.load("assets/textures/background.png")
bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_pos = 0


def draw_bg():
	global bg_pos
	screen.blit(bg, (0, bg_pos))
	screen.blit(bg, (0, bg_pos - SCREEN_HEIGHT))
	if bg_pos == SCREEN_HEIGHT:
		bg_pos = 0
	bg_pos += 1
	
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SHIP_SPEED = 8
PROJECTILE_COOLDOWN = 200
HEALTH = 3

ship_group = pygame.sprite.Group()
ship = Ship(int(SCREEN_WIDTH / 2), 90/100*SCREEN_HEIGHT, HEALTH)
#ship.setScale(2)
ship_group.add(ship)

health_group = pygame.sprite.Group()
#healthBar = HealthBar()
#health_group.add(healthBar)

PROJECTILE_SPEED = 10
proj_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

ROWSENEMY = 2
COLUMNSENEMY = 5

for i in range(0, ROWSENEMY):
	for j in range(0, COLUMNSENEMY):
		enemy = Enemy(10/100 * SCREEN_WIDTH + 80/100*SCREEN_WIDTH/(COLUMNSENEMY - 1) * j, 12/100 * SCREEN_HEIGHT * (i + 1), 3)
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

	ship.update(proj_group, enemy_group, SHIP_SPEED, PROJECTILE_COOLDOWN)
	ship_group.draw(screen)

	enemy_group.draw(screen)

	proj_group.update(PROJECTILE_SPEED, enemy_group)
	proj_group.draw(screen)

	score = (initNoEnemies - len(enemy_group.sprites())) * ENEMYVALUE

	if ship.ok == 1:
		txtsurf = font.render("Score: " + str(score), True, (255, 255, 255))
		screen.blit(txtsurf, (0, 0))
	else:
		txtsurf = font.render("Dead", True, (255, 0, 0))
		screen.blit(txtsurf, (0, 0))

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
