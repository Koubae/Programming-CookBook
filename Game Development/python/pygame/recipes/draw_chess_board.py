block_size = 16
recs = []
for x in range(0, self.WIN_WIDTH, block_size):
    for y in range(0, self.WIN_HEIGHT, block_size):
        rect = pygame.Rect(x, y, block_size, block_size)
        pygame.draw.rect(self.window, (255, 255, 255), rect, 1)
        recs.append(rect)
pg.display.update(recs)