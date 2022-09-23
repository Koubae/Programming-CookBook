import pygame as pg
from pygame.math import Vector2

# pygame constants
CLOCK = pg.time.Clock()
WIN_SIZE = (1280, 640)
# pygame setup
pg.init()
# screen
window = pg.display.set_mode(WIN_SIZE, 0, 32)
background = pg.Surface(WIN_SIZE)

player = pg.Surface(Vector2(12, 64))
player_rect = player.get_rect(topleft=Vector2(150, 150))
player_attack = False
player.fill((102, 255, 178))
player_attack_range = 20 # player can hit at min 20 pixel from target

enemy = pg.Surface(Vector2(12, 64))
enemy_rect = player.get_rect(topleft=Vector2(175, 150))
enemy.fill(pg.Color("green"))

while True:
    background.fill((0, 0, 0))  # screen clear

    # Render enemy
    attacked = False
    if player_attack:
        # !!!!! HERE !!!!!
        # Now we check if the playuer is close enough to the enemy, so we MUST know the enemy pos
        distance_x = abs(player_rect.x - enemy_rect.x)
        if distance_x > player_attack_range:
            attacked = True
            enemy.fill(pg.Color("red"))
    if not attacked:
        enemy.fill(pg.Color("green"))

    background.blit(enemy, enemy_rect.topleft)
    # Render player
    background.blit(player, player_rect.topleft)


    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):  # x button and esc terminates the game!
            exit(1)
        # ............. Mouse ............. #
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_attack = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                player_attack = False

    pg.display.update()  # 2) Update the game
    window.blit(background, (0, 0))  # 3) Repaint the screen
    CLOCK.tick(60)  # 4) Wait 60 Frames


