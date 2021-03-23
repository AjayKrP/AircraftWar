#!bin/python3
import pygame

"""
This is a Game Config File
"""

pygame.mixer.init()

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT = (170,170,170)
COLOR_DARK = (100,100,100)
BACKGROUND_COLOR = (135, 206, 250)

move_up_sound = pygame.mixer.Sound('music/Rising_putter.ogg')
move_down_sound = pygame.mixer.Sound("music/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("music/Collision.ogg")

