# -----!!!!SPACE INVADERS!!!!-----
from spaceship import *
from random import randint
import pygame
from pygame.locals import *
import time
from threading import Timer


# ---------------------colours-----------------
Green = (0, 255, 0)


# -----------main game class------------------
class Game():
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.mouse.set_visible(False)
        self.ship = Ship(self.screen.get_rect())
        self.enemies = []
        self.enemies.append(Enemy(randint(0, 7)*100, randint(0, 1)*100))
        font = pygame.font.SysFont("", 72)
        self.text_paused = font.render("PAUSED", True, (255, 0, 0))
    # -----MAIN GAME LOOP-----

    def run(self):
        # --------------------------
        font = pygame.font.SysFont("", 30)
        clock = pygame.time.Clock()
        RUNNING = True
        PAUSED = False
        start_time = time.time()
        while RUNNING:
            clock.tick(60)  # 60 fps
        # ---------------------------------
            # --- events ---
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        RUNNING = False
                    if event.key == K_ESCAPE:
                        RUNNING = False

                    if event.key == K_p:
                        PAUSED = not PAUSED

                if not PAUSED:
                    self.ship.event_handler(event)
            # --- if game not paused
            if not PAUSED:
                self.ship.update()

                for e in self.enemies:
                    e.update()

                self.ship.bullet_detect_collison(self.enemies)

                for i in range(len(self.enemies)-1, -1, -1):
                    end = time.time()
                    if not self.enemies[i].is_alive:
                        # print "debug: Ship.update: removing bullet ", i
                        del self.enemies[i]
                    elif end - self.enemies[i].start >= 8:
                        del self.enemies[i]

                end_time = time.time()
                if end_time-start_time > 10:
                    self.enemies.append(Enemy(randint(0, 7)*100, randint(0, 1)*100))
                    start_time = time.time()
            # --- drawing things on screen---
            self.screen.fill((0, 0, 0))
            self.score_game = font.render("score={}".format(self.ship.score), True, (Green))
            self.ship.draw(self.screen)
            self.screen.blit(self.score_game, (0, 0))
            for e in self.enemies:
                e.draw(self.screen)

            if PAUSED:
                self.screen.blit(self.text_paused, (300, 400))
                self.screen.blit(self.score_game, (350, 350))
            pygame.display.update()

        # --- quit ---
        pygame.quit()


# -------------running the game---------------
Game().run()
