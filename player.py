# -----!!!!SPACE INVADERS!!!!-----
import random
import pygame
from pygame.locals import *
import time
from threading import Timer
Green = (0, 255, 0)


class Enemy():

    def __init__(self, x, y):

        self.image = pygame.image.load("image/alien.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x+50
        self.rect.centery = y+50
        self.is_alive = True
        self.start = time.time()
    # --------------------

    def update(self):
        if self.rect.y > 200:
            self.is_alive = False
    # --------------------

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def bull(self):
        end = time.time()
        self.image = pygame.image.load("image/alien2.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
