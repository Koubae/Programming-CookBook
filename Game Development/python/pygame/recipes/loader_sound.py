"""Simple script that imports assets sounds"""

import pygame as pg
from typing import Union
import os

# Load configurations
DIR_GAME = os.path.split(os.path.abspath(__file__))[0]
DIR_ASSETS = os.path.join(DIR_GAME, "assets")


ASSETS_SOUNDS = "sounds"

class SoundDummy:
    """Dummy class that implements the pg.mixer.Sound interface
        To be used when a sound asset is not found or for testing
    """

    def play(self):
        pass


def loader_sound(name: str) -> Union[pg.mixer.Sound, SoundDummy]:
    """Loads a sound

    :param name: FIle name of the sound
     @throws FileNotFoundError If assets is not found
    :return:
    """
    if not pg.mixer or not pg.mixer.get_init():
        return SoundDummy()

    try:
        fullname = os.path.join(DIR_ASSETS, ASSETS_SOUNDS, name)
        sound = pg.mixer.Sound(fullname)
    except FileNotFoundError as err:
        print(f"Error while loading sound {name} \n {err}")
        raise err

    return sound