"""Minimum app that shows how to set font and font family
@credit: https://stackoverflow.com/a/64487335/13903942
"""

import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((500, 150))
clock = pygame.time.Clock()

ft_font = pygame.freetype.SysFont('Times New Roman', 80)

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    text_rect = ft_font.get_rect('Hello World')
    text_rect.center = window.get_rect().center
    ft_font.render_to(window, text_rect.topleft, 'Hello World', (255, 0, 0))
    pygame.display.flip()

pygame.quit()
exit()