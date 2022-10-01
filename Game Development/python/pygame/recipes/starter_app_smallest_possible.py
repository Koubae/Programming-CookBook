"Smalles pygame app possible"
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

    pygame.draw.line(window, pygame.Color("white"), [150, 325], [500, 325], 2)

    pygame.display.flip()
    clock.tick(60)
