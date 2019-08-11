"""
Towers.py
Creates classes for all six towers
"""

import pygame
import sys
import random
import math
from random import uniform
from os import path

from settings import *
from Bullet import *

#Parent class for all towers
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.imageT1
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center

    def get_keys(self):
        pass

    def update(self):
        pass

#Represents the Path that the balloons must follow
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

#Tower 1
class Tower1(pygame.sprite.Sprite):

    #load image, dimensions of tower
    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.name = "Tower1"
        self.slowed = False
        self.current = 0
        self.dir = 0

    def get_keys(self):
        #check what direction the bullet should fire
        if(self.game.direction1%4==0):
            self.dir = (1,0)
        elif(self.game.direction1%4==1):
            self.dir = (0,1)
        elif(self.game.direction1%4==2):
            self.dir = (-1,0)
        elif(self.game.direction1%4==3):
            self.dir = (0,-1)

        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):
        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time1):
            self.get_keys()
            self.current = spawn_time

class Tower2(pygame.sprite.Sprite):

    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT2
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.name = "Tower2"
        self.slowed = False
        self.current = 0
        self.dir = 0

    def get_keys(self):

        #check what direction the bullet should fire
        if(self.game.direction2%4==0):
            self.dir = (1,0)
        elif(self.game.direction2%4==1):
            self.dir = (0,1)
        elif(self.game.direction2%4==2):
            self.dir = (-1,0)
        elif(self.game.direction2%4==3):
            self.dir = (0,-1)

        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):

        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time2):
            self.get_keys()
            self.current = spawn_time

class Tower3(pygame.sprite.Sprite):

    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT3
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.slowed = False
        self.name = "Tower3"
        self.current = 0
        self.dir = 0

    def get_keys(self):

        #check what direction the bullet should fire
        if(self.game.direction3%4==0):
            self.dir = (1,0)
        elif(self.game.direction3%4==1):
            self.dir = (0,1)
        elif(self.game.direction3%4==2):
            self.dir = (-1,0)
        elif(self.game.direction3%4==3):
            self.dir = (0,-1)
        
        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):

        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time3):
            self.get_keys()
            self.current = spawn_time

class Tower4(pygame.sprite.Sprite):

    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT4
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.slowed = False
        self.name = "Tower4"
        self.current = 0
        self.dir = 0

    def get_keys(self):
        
        #check what direction the bullet should fire
        if(self.game.direction4%4==0):
            self.dir = (1,0)
        elif(self.game.direction4%4==1):
            self.dir = (0,1)
        elif(self.game.direction4%4==2):
            self.dir = (-1,0)
        elif(self.game.direction4%4==3):
            self.dir = (0,-1)
        
        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):

        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time4):
            self.get_keys()
            self.current = spawn_time

class Tower5(pygame.sprite.Sprite):

    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT5
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.slowed = False
        self.current = 0
        self.name = "Tower5"
        self.dir = 0

    def get_keys(self):
        
        #check what direction the bullet should fire
        if(self.game.direction5%4==0):
            self.dir = (1,0)
        elif(self.game.direction5%4==1):
            self.dir = (0,1)
        elif(self.game.direction5%4==2):
            self.dir = (-1,0)
        elif(self.game.direction5%4==3):
            self.dir = (0,-1)
        
        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):

        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time5):
            self.get_keys()
            self.current = spawn_time

class Tower6(pygame.sprite.Sprite):

    def __init__(self, game,color,x,y):
        super(Player).__init__()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = color
        self.image = game.imageT6
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.slowed = False
        self.distance = 0
        self.current = 0
        self.name = "Tower6"
        self.dir = 0

    def get_keys(self):

        #check what direction the bullet should fire
        if(self.game.direction6%4==0):
            self.dir = (1,0)
        elif(self.game.direction6%4==1):
            self.dir = (0,1)
        elif(self.game.direction6%4==2):
            self.dir = (-1,0)
        elif(self.game.direction6%4==3):
            self.dir = (0,-1)
        
        #if start button clicked, then fire bullets
        if(self.game.startWave):
            Bullet(self.game,self.rect.centerx, self.rect.top,self.name,self.dir)

    def update(self):

        #self.game.time1 represents how many bullets comes out in a certain set of time
        #increases when upgraded
        spawn_time = pygame.time.get_ticks()
        if(spawn_time-self.current>=self.game.time6):
            self.get_keys()
            self.current = spawn_time