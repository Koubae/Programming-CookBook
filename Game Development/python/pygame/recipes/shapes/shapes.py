"Different Shapes"
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((1280, 650), 0, 32)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit(0)
    window.fill(pygame.Color("black"))  # repaints

    # 3 Lines
    # no rectangle
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 25), (50 - 25, 50 - 25)))
    # equilateral
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 25)))
    # long
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 85)))
    # squish
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 25), (45,45)))

    # 4 lines
    # Thunder??
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 25), (50+25, 25)))

    # rhomboid
    # pg.draw.polygon(background, (0, 255, 175), ((50, 50), (50 + 25, 50 + 25), (50, 50 + 25 + 25), (25, 50+25)))

    pygame.display.flip()
    clock.tick(60)
