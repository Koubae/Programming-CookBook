# music_manager.py
import pygame
from pygame.locals import *


class MusicManager:
    def __init__(self):
        super().__init__()
        self.volume = 0.05  # Default Volume

    def playsoundtrack(self, music, num, vol):
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(num)

    def playsound(self, sound, vol):
        sound.set_volume(vol)
        sound.play()

    def stop(self):
        pygame.mixer.music.stop()


# main.py

from music_manager import MusicManager

# freq, size, channel, buffsize
pygame.mixer.pre_init(44100, 16, 1, 512)
pygame.init()


# Music and Sound
soundtrack = ["background_village.wav", "battle_music.wav", "gameover.wav"]
swordtrack = [pygame.mixer.Sound("sword1.wav"), pygame.mixer.Sound("sword2.wav")]
fsound = pygame.mixer.Sound("fireball_sound.wav")
hit = pygame.mixer.Sound("enemy_hit.wav")

mmanager = MusicManager()
mmanager.playsoundtrack(soundtrack[0], -1, 0.05)


# playing

def world1(self):
    self.world = 1
    ...
    mmanager.playsoundtrack(soundtrack[1], -1, 0.05)


def world2(self):
    self.world = 2
    ...
    mmanager.playsoundtrack(soundtrack[1], -1, 0.05)


def world3(self):
    self.world = 3
    ...
    mmanager.playsoundtrack(soundtrack[1], -1, 0.05)

    def attack(self):
        if cursor.wait == 1: return

        # If attack frame has reached end of sequence, return to base frame
        if self.attack_frame > 10:
            self.attack_frame = 0
            self.attacking = False

        if self.attack_frame == 0:
            mmanager.playsound(swordtrack[self.slash], 0.05)

            self.slash += 1
            if self.slash >= 2:
                self.slash = 0