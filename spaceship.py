# -----!!!!SPACE INVADERS!!!!-----
import random
import pygame
import time
from pygame.locals import *
from threading import Timer
from player import *
from ammunations import *

# ------------defining colours----------------------
Green = (0, 255, 0)


# ------------------spaceship class----------------------------
class Ship():

    def __init__(self, screen_rect):

        self.image = pygame.image.load("image/spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_rect.bottom-100
        self.rect.centerx = screen_rect.centerx
        self.move_x = 0
        self.shots = []
        self.missiles = []
        self.uptime = time.time()
        self.score = 0
    # --------------------

    def event_handler(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a:
                self.move_x = -20
            elif event.key == K_d:
                self.move_x = 20
            elif event.key == K_s:
                self.shots.append(Bullet1(self.rect.centerx, self.rect.top))
            elif event.key == K_SPACE:
                self.missiles.append(Bullet2(self.rect.centerx, self.rect.top))
        if event.type == KEYUP:
            if event.key in (K_a, K_d):
                self.move_x = 0
    # ---------------------------

    def update(self):

        if (self.rect.centerx > 50 or self.move_x > 0) and (self.rect.centerx < 750 or self.move_x < 0):
            self.rect.x += self.move_x
        for s in self.shots:
            s.update()
        for m in self.missiles:
            m.update()
    # --------------------

    def draw(self,  screen):
        screen.blit(self.image,  self.rect.topleft)
        for s in self.shots:
            s.draw(screen)
        for m in self.missiles:
            m.draw(screen)
    # ------------------------

    def bullet_detect_collison(self, enemy_list):
        global score
        temp = []

        def fuck():
            for i in temp:
                i.image = pygame.image.load("image/alien.png")
                i.image = pygame.transform.scale(i.image, (100, 100))
        for s in self.shots:
            for e in enemy_list:
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    temp.append(e)
                    e.start += 5
                    e.bull()
        for m in self.missiles:
            for e in enemy_list:
                if pygame.sprite.collide_circle(m, e):
                    m.is_alive = False
                    e.is_alive = False
                    self.score += 1
        t = Timer(5, fuck)
        t.start()
        for i in range(len(self.missiles)-1, -1, -1):
            if not self.missiles[i].is_alive:
                del self.missiles[i]

        for i in range(len(self.shots)-1, -1, -1):
            if not self.shots[i].is_alive:
                del self.shots[i]

    # ---------------end---------------
