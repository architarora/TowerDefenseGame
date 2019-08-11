"""
Bullet.py
Represents the different type of bullets that each tower shoots 
"""

import pygame
import sys
import random
import math
from random import uniform
from os import path

from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x,y ,name,direction):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = name
        self.indicateDirection = direction
        #Different bullet types, damage, and sounds based on which tower
        #is firing the bullets
        if(self.name=="Tower1"):
            self.image = game.bullet_basketball
            game.damage = Tower1Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_1
        elif(self.name == "Tower2"):
            self.image = game.bullet_soccer
            game.damage = Tower2Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_2
        elif(self.name == "Tower3"):
            self.image = game.bullet_volley
            game.damage = Tower3Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_3
        elif(self.name == "Tower4"):
            self.image = game.bullet_golf
            game.damage = Tower4Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_4
        elif(self.name == "Tower5"):
            self.image = game.bullet_tennis
            game.damage = Tower5Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_5
        elif(self.name == "Tower6"):
            self.image = game.bullet_football
            game.damage = Tower6Damage
            game.soundType = self.name
            self.lifeTime = BULLET_LIFETIME_6

        #responsible for moving the bullet
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -10
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        
        #based on direction, move the bullet
        if(self.indicateDirection==(1,0)):
            self.speedx = -10
            self.speedy = 0
        elif(self.indicateDirection == (0,1)):
            self.speedx = 0
            self.speedy = -10
        elif(self.indicateDirection == (-1,0)):
            self.speedx = 10
            self.speedy = 0
        elif(self.indicateDirection == (0,-1)):
            self.speedx = 0
            self.speedy = 10

        self.rect.y -= self.speedy
        self.rect.x -= self.speedx

        #acts as the range for the bullet, can only go on the screen
        #for. definite amount of time, otherwise remove the bullet
        if pygame.time.get_ticks() - self.spawn_time > self.lifeTime:
            self.kill()
