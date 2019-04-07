import pygame,sys
from pygame.locals import *
#--defining colours
Black=(0,0,0)
White=(255,255,255)
Green=(0,255,0)
Blue=(0,0,255)#or 128
Red=(255,0,0)
Purple=(255,0,255)
#--defining missile
class missile():
    def __init__(self):
        super(Bullet, self).__init__()
        self.image = pygame.Surface([4, 15])
        self.image.fill(Red)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 12

class Bullet():

    def __init__(self, x, y):

        #self.image = pygame.image.load("SingleBullet.png")
        self.image = pygame.image.load("i.jpg")
        self.image = pygame.transform.scale(self.image, (25,25))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #--------------------

    def update(self):

        self.rect.y -= 100

        if self.rect.y < 0:
            self.is_alive = False

    #--------------------

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
