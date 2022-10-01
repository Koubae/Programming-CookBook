import pygame as pg
import pygame.font
from pygame.math import Vector2
import sys


def run():
    # pygame constants
    CLOCK = pg.time.Clock()
    FRAMES: int = 60

    # world
    FLOOR_CHUNK = 64
    SCREEN_SIZE = ["small", "medium", "large"]
    SCREEN_SELECT = SCREEN_SIZE[1]
    if SCREEN_SELECT == "medium":
        WIN_WIDTH = FLOOR_CHUNK * 20   # 1280
        WIN_HEIGHT = FLOOR_CHUNK * 10  # 640
    elif SCREEN_SELECT == "large":
        WIN_WIDTH = FLOOR_CHUNK * 30   # 1920
        WIN_HEIGHT = FLOOR_CHUNK * 20  # 1280
    else:
        WIN_WIDTH = FLOOR_CHUNK * 10   # 640
        WIN_HEIGHT = FLOOR_CHUNK * 5   # 320

    WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)

    # pygame setup
    pg.init()
    pg.display.set_caption("Drawings")

    # screen
    window = pg.display.set_mode(WIN_SIZE, 0, 32)
    background = pg.Surface(WIN_SIZE)

    # entities
    def load_fonts() -> list:
        fonts = []
        pygame_fonts = pg.font.get_fonts()
        pygame_fonts.sort()
        for font_family in pygame_fonts:
            try:
                font = pygame.font.SysFont(font_family, 22)
            except FileNotFoundError as err:
                print(f'{font_family} not found in system -> {str(err)}')
                continue
            font_img = font.render(font_family, True, (255, 255, 255))
            fonts.append((font_family, font_img, font))
        return fonts

    fonts = load_fonts()


    # Game data
    game_data = {
        'run': True
    }
    scroll_y = 0
    scroll_strength = 50
    # handlers
    def events_handler():
        nonlocal  scroll_y

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):  # x button and esc terminates the game!
                game_data["run"] = False

            if event.type == pg.MOUSEWHEEL:
                if event.y == 1:
                    scroll_y -= scroll_strength
                else:
                    scroll_y += scroll_strength


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
        for i, f in enumerate(fonts):
            font_family, font_img, font = f
            background.blit(font_img,
                                     Vector2(WIN_WIDTH / 2 - 24, (i * 55) - scroll_y))




        # ==============================================================================
        # ..............................................................................
        # ==============================================================================

        # This in order
        events_handler()    # 1) Evebts
        game_update()       # 2) Update the game
        screen_paint()      # 3) Repaint the screen
        game_tick()         # 4) Wait 60 Frames

    # Do some resource clean up ...
    pg.quit()
    sys.exit(0)


if __name__ == '__main__':
    ONLY_PRINT = False
    if ONLY_PRINT:
        print(pg.font.get_fonts())
    else:
        run()

