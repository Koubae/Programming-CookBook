"""Simple script that imports assets sprites"""

import os
import pygame as pg
from typing import Union
import os

# Load configurations
DIR_GAME = os.path.split(os.path.abspath(__file__))[0]
DIR_ASSETS = os.path.join(DIR_GAME, "assets")

def loader_sprite(name: str, colorkey: Union[int, tuple] = None, scale: int = 1) -> tuple:
    """Loads a Sprite in memory

    :param name: str Name of sprite to import
    :param colorkey: -1  lookup the color at the topleft pixel of the image, and use that color for the colorkey.
    else a tuple as RGB value, example (255, 255, 255)
    :param scale: int Scale of the sprite, 1 means original scale

    @throws FileNotFoundError If assets is not found
    :return:
    """
    try:
        fullname = os.path.join(DIR_ASSETS, name)
        image = pg.image.load(fullname)
    except FileNotFoundError as err:
        print(f"Error while loading sprite {name} \n {err}")
        raise err

    else:
        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pg.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image, image.get_rect()
