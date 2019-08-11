"""
Enemy.py
Creates and moves the enemy (balloons) throughout the screen
"""

import pygame
import sys
import random
import math
from random import uniform
from os import path

from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites, game.enemy
        pygame.sprite.Sprite.__init__(self)
        #based on balloonStren in Game Class, health and image of balloon get selected
        if (bloonTypes[game.balloonStren]["color"]=="red"):
            self.image = game.balloon_red
            self.health = 20
        elif (bloonTypes[game.balloonStren]["color"]=="purple"):
            self.image = game.balloon_purple
            self.health = 40
        elif (bloonTypes[game.balloonStren]["color"]=="blue"):
            self.image = game.balloon_blue
            self.health = 60
        elif (bloonTypes[game.balloonStren]["color"]=="yellow"):
            self.image = game.balloon_yellow
            self.health = 80
        elif (bloonTypes[game.balloonStren]["color"]=="moab"):
            self.image = game.balloon_moab
            self.health = 170
            game.balloonStren-=1
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.speedy = 5
        self.speedx = 5
        self.damageMultiplier = 1
        self.distance = 0
        self.speedBalloon = 5 

    def update(self):

        #coordinates of the balloon
        x = self.rect.x
        y = self.rect.y

        #get the row and column of the balloon
        (row,col) = self.game.getCell(x,y)

        #check what the image and balloon speed should be based on
        #the health of the balloon
        if(self.health>80):
            self.image = self.game.balloon_moab
            self.damageMultiplier = 5
            self.speedBalloon = self.game.speedMOAB
        elif(self.health<=80 and self.health>60):
            self.image = self.game.balloon_yellow
            self.damageMultiplier = 4
            self.speedBalloon = self.game.speedYELLOW 
        elif(self.health<=60 and self.health>40):
            self.image = self.game.balloon_blue
            self.damageMultiplier = 3
            self.speedBalloon = self.game.speedBLUE 
        elif(self.health<=40 and self.health>20):
            self.image = self.game.balloon_purple
            self.damageMultiplier = 2
            self.speedBalloon = self.game.speedPURPLE
        elif(self.health<=20 and self.health>0):
            self.image = self.game.balloon_red
            self.damageMultiplier = 1
            self.speedBalloon = self.game.speedRED 

        #moves the balloon
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        #Based on map, find the coordinates where the direction of the balloon
        #should be changed
        if(self.game.strMap=="map.txt"):
            if((row,col)==(0,0)):
                self.speedx = 0
            if((row,col)==(4,0)):
                self.speedy=0
                self.speedx = self.speedBalloon
            if((row,col)==(4,6)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(10,6)):
                self.speedy = 0
                self.speedx = self.speedBalloon
            if((row,col)==(10,11)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(11,11)):
                self.game.lives-=(1/10)*self.damageMultiplier
        #Based on map, find the coordinates where the direction of the balloon
        #should be changed
        if(self.game.strMap == "map2.txt"):
            if((row,col)==(0,0)):
                self.speedx = 0
            if((row,col)==(3,0)):
                self.speedy=0
                self.speedx = self.speedBalloon
            if((row,col)==(3,1)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(8,1)):
                self.speedy = 0
                self.speedx = self.speedBalloon
            if((row,col)==(8,7)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(10,7)):
                self.speedy = 0
                self.speedx = self.speedBalloon
            if((row,col)==(10,10)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(11,10)):
                self.game.lives-=(1/10)*self.damageMultiplier
        #Based on map, find the coordinates where the direction of the balloon
        #should be changed
        if(self.game.strMap == "map3.txt"):
            if((row,col)==(0,0)):
                self.speedx = 0
            if((row,col)==(9,0)):
                self.speedy=0
                self.speedx = self.speedBalloon
            if((row,col)==(9,11)):
                self.speedy = self.speedBalloon
                self.speedx = 0
            if((row,col)==(11,11)):
                self.game.lives-=(1/10)*self.damageMultiplier

        #remove the balloon off the screen if the health is 0
        if(self.health<=0):
            self.kill()