# --------------importing modules----------------
import random
import pygame
from pygame.locals import *
import time
from threading import Timer

# -----------defining colors--------
Green = (0, 255, 0)
# --------------definng main missiles class--------------


class Missiles():
    global score

    def __init__(self, x, y):

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.is_alive = True

# -------------------bullet 1 class-------------------------(fast bullet)


class Bullet1(Missiles):

    def __init__(self, x, y):

        self.image = pygame.image.load("image/bull.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        super().__init__(x, y)

    # --------------------

    def update(self):
        self.rect.y -= 10

        if self.rect.y > 200 and self.rect.y < 0:
            self.is_alive = False

    # --------------------

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


# ------------------bullet 2 clss----------------(slow bullet)
class Bullet2(Missiles):
    def __init__(self, x, y):
        self.image = pygame.image.load("image/rocket.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        super().__init__(x, y)
    # ------------------------------------

    def update(self):
        self.rect.y -= 5

        if self.rect.y < 0 and self.rect.y > 200:
            self.is_alive = False

    # -----------------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
