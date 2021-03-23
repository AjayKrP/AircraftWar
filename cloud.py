#!bin/python3

import pygame
from config import *
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        pygame.display.set_mode()
        self.surf = pygame.image.load('images/cloud.png').convert()
        self.surf.set_colorkey(COLOR_WHITE, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
