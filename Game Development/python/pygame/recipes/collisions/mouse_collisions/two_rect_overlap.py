"""@credit -> https://stackoverflow.com/a/65064907/13903942"""
import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))
rect1 = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
rect2 = pygame.Rect(0, 0, 75, 75)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    color = (255, 0, 0) if collide else (255, 255, 255)

    window.fill(0)
    pygame.draw.rect(window, color, rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2, 6, 1)
    pygame.display.flip()

pygame.quit()
exit()