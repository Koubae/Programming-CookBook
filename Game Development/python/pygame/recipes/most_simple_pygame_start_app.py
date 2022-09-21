import pygame as pg
from pygame.math import Vector2


def run():
    # pygame constants
    CLOCK = pg.time.Clock()
    FRAMES: int = 60
    WIN_WIDTH = 1280
    WIN_HEIGHT = 640
    WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)

    # pygame setup
    pg.init()
    pg.display.set_caption("Drawings")

    # screen
    window = pg.display.set_mode(WIN_SIZE, 0, 32)
    background = pg.Surface(WIN_SIZE)

    # entities
    FLOOR_CHUNK = 64
    FLOOR_SIZE = Vector2(FLOOR_CHUNK, FLOOR_CHUNK)
    floor_tiles = [pg.Rect(x * FLOOR_CHUNK, FLOOR_CHUNK *  8, FLOOR_CHUNK, FLOOR_CHUNK) for x in range(25)]

    # Game data
    game_data = {
        'run': True
    }

    # handlers
    def events_handler():

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):  # x button and esc terminates the game!
                game_data["run"] = False

    screen_clear = lambda: background.fill((0, 0, 0))
    screen_paint = lambda: window.blit(background, (0, 0))
    game_update = lambda: pg.display.update()
    game_tick = lambda: CLOCK.tick(FRAMES)

    triangle_increase = 0
    triangle_point_1 = 25

    circle_roll = 0
    circle_x = 155


    while game_data["run"]:
        screen_clear()  # screen clear

        # ==============================================================================
        #                               GAME LOGIC HERE
        # ==============================================================================

        # Render entities
        for i, tile in enumerate(floor_tiles):
            img = pg.Surface(FLOOR_SIZE)
            if i % 2 == 0:
                img.fill((75, 75, 175))
            else:
                img.fill((255, 250, 60))

            background.blit(img, tile.topleft)


        # Draw stuff
        if triangle_increase > 20:
            triangle_increase = 20
            triangle_point_1 += 1
        else:
            triangle_increase += 1

        if circle_roll > 5:
            circle_roll = 0
            circle_x += 20
        else:
            circle_roll += 1

        # square
        pg.draw.rect(background, (255, 0, 0), pg.Rect(Vector2(155, 390), Vector2(120, 120)))
        # Rectangle
        pg.draw.rect(background, (255, 255, 75), pg.Rect(Vector2(WIN_WIDTH / 2, WIN_HEIGHT / 2), Vector2(200, 150)))
        # Triangle
        pg.draw.polygon(background, (0, 255, 175), ((triangle_point_1, 25), (320, 125), (250, 390)))
        # Circle
        pg.draw.circle(background, (0, 255, 0), Vector2(circle_x, 200), 140)
        # Elispe 1 ( Inside square )
        pg.draw.ellipse(background, (50, 120, 120), pg.Rect(Vector2(155, 390), Vector2(120, 120)), 200)
        # Elispe 2
        pg.draw.ellipse(background, (50, 120, 120), pg.Rect(Vector2(800, 100), Vector2(99, 320)), 200)
        # Line 1
        pg.draw.line(background, (255, 255, 255), Vector2(850, 50), Vector2(10, 500))
        pg.draw.line(background, (255, 255, 255), Vector2(50, 850), Vector2(500, 10))
        # Lines
        pg.draw.lines(background, (0, 120, 245), True, (Vector2(980, 320), Vector2(235, 560)), width=20)


        # ==============================================================================
        # ..............................................................................
        # ==============================================================================

        # This in order
        events_handler()    # 1) Evebts
        game_update()       # 2) Update the game
        screen_paint()      # 3) Repaint the screen
        game_tick()         # 4) Wait 60 Frames


if __name__ == '__main__':
    run()
