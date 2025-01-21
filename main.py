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

score = 0
oldScore = 0
ENEMYVALUE = 5
initNoEnemies = 0

font = pygame.font.SysFont("Arial", 32)

def start_new_level(level):
    global enemy_group, initNoEnemies, health, ship, ship_group, proj_group, ui_group, healthBar

    enemy_group.empty()
    proj_group.empty()
    ship_group.empty()
    ui_group.empty()

    ship = Ship(int(Settings.SCREEN_WIDTH / 2), 90/100*Settings.SCREEN_HEIGHT)
    ship_group.add(ship)

    healthBar = HealthBar()
    ui_group.add(healthBar)

    if (level > 4):
        ROWSENEMY = 4
    else:
        ROWSENEMY = level
    COLUMNSENEMY = 12
    for i in range(0, ROWSENEMY):
        for j in range(0, COLUMNSENEMY):
            enemy = Enemy(-0.9 * Settings.SCREEN_WIDTH + 1.8*Settings.SCREEN_WIDTH/(COLUMNSENEMY - 1) * j, 0.12 * Settings.SCREEN_HEIGHT * (i + 1), 3)
            enemy_group.add(enemy)
	
    initNoEnemies = len(enemy_group.sprites())

level = 1

#game loop
run = True
while run:
	clock.tick(FPS)
	draw_bg()

	ship.update(proj_group, enemy_group)
	ship_group.draw(screen)

	enemy_group.update(level)
	enemy_group.draw(screen)

	proj_group.update(enemy_group)
	proj_group.draw(screen)

	ui_group.draw(screen)

	healthBar.setHealth(health)

	score = oldScore + (initNoEnemies - len(enemy_group.sprites())) * ENEMYVALUE

	if ship.ok != 1 and health > 0:
		health-=1
		ship = Ship(int(Settings.SCREEN_WIDTH / 2), 90/100*Settings.SCREEN_HEIGHT)
		ship_group.add(ship)

	if health != 0:
		txtsurf = font.render("Score: " + str(score), True, (255, 255, 255))
		screen.blit(txtsurf, (Settings.SCREEN_WIDTH - 150, 0))
	else:
		ship.kill()
		txtsurf = font.render("DIED!", True, (255, 0, 0))
		screen.blit(txtsurf, (Settings.SCREEN_WIDTH / 2 - 37, Settings.SCREEN_HEIGHT / 2))
		txtsurf = font.render("Score: " + str(score), True, (255, 255, 255))
		screen.blit(txtsurf, (Settings.SCREEN_WIDTH / 2 - 60, Settings.SCREEN_HEIGHT / 2 - 30))

	if len(enemy_group.sprites()) == 0:
		oldScore += score
		level += 1
		start_new_level(level)

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
