"""
settings.py
File contains all constants used in all of the classes
"""

import pygame

BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

vec = pygame.math.Vector2
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
BULLET_SPEED = 300
BULLET_LIFETIME_1 = 1000
BULLET_LIFETIME_2 = 1200
BULLET_LIFETIME_3 = 1400
BULLET_LIFETIME_4 = 1600
BULLET_LIFETIME_5 = 1800
BULLET_LIFETIME_6 = 2000
BULLET_RATE = 20

MAROON = (128,0,0)
RED = (255, 0, 0)
AQUA = (0,255,255)
PURPLE = (128,0,128)
WHITE = (255, 255, 255)
BROWN = (255,235,205)
LIGHTBROWN = (222,184,135)


MONEYBALLOONHIT = 15

WIDTH = 1024  
HEIGHT = 768  
FPS = 60
TITLE = "Bloons Tower Defense"
BGCOLOR = DARKGREY
FONT_NAME = 'arial'

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

ROWS = 12
COLS = 16

CREATINGBUTTONX = (46,285)
CREATINGBUTTONY = (581,614)

bloons = {
"red":
{"strength": 1,
"speed": 2,},
"blue":
{
"strength": 2,
"speed": 3,
},
"green":
{
"strength": 3,
"speed": 4,
},
"yellow":
{
"strength": 4,
"speed": 5,
},
"pink":
{
"strength": 5,
"speed": 6,
},
}

Tower1X = (769,831)
Tower1Y = (162,231)

Tower2X = (769,831)
Tower2Y = (310,384)

Tower3X = (769,831)
Tower3Y = (482,549)

Tower4X = (896,958)
Tower4Y = (162,231)

Tower5X = (896,958)
Tower5Y = (310,384)

Tower6X = (896,958)
Tower6Y = (482,549)

StartButX = (818,933)
StartButY = (600,632)

TOWER1PRICE = 400
TOWER2PRICE = 500
TOWER3PRICE = 600
TOWER4PRICE = 700
TOWER5PRICE = 800
TOWER6PRICE = 900

UPGRADE1X = (750,851)
UPGRADE1Y = (236,260)

UPGRADE2X = (750,851)
UPGRADE2Y = (400,418)

UPGRADE3X = (750,851)
UPGRADE3Y = (557,574)

UPGRADE4X = (874,982)
UPGRADE4Y = (236,260)

UPGRADE5X = (874,982)
UPGRADE5Y = (400,418)

UPGRADE6X = (874,982)
UPGRADE6Y = (557,574)

towerTypes = {
    #cooldown in seconds, range is radius around monkey
    "Tower1": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "basketball",
        "description": "Basketball Tower",
        "price": TOWER1PRICE
        },
    "Tower2": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "soccer",
        "description": "Soccer Tower",
        "price": TOWER2PRICE
        },
    "Tower3": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "volley",
        "description": "Volley Tower",
        "price": TOWER3PRICE
        },
    "Tower4": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "golf",
        "description": "Freeze Tower",
        "price": TOWER4PRICE
        },
    "Tower5": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "tennis",
        "description": "Tennis Tower",
        "price": TOWER5PRICE
        },
    "Tower6": 
        {
        "damage": 1, 
        "slow": 0, 
        "range": 125,
        "bullet": "Football",
        "description": "Football Tower",
        "price": TOWER6PRICE
        },
    "None":
    	{
    	"description": "No Tower Selected",
    	"price": "No Tower Selected"
    	}
  }

LEVEL1TIME = 25
LEVEL2TIME = 65
LEVEL3TIME = 95
LEVEL4TIME = 120
LEVEL5TIME = 150
GAMEOVERTIME = 155

bloonTypes = {
	1: {"color": "red","speed":5},
    2: {"color": "purple","speed":8},
    3: {"color": "blue","speed":12},
    4: {"color": "yellow","speed":15},
    5: {"color": "moab", "speed":15}
}

SPEEDBALLOONRED = 5
SPEEDBALLOONPURPLE = 8
SPEEDBALLOONBLUE = 12
SPEEDBALLOONYELLOW = 15

Tower1Damage = 10
Tower2Damage = 13
Tower3Damage = 18
Tower4Damage = 25
Tower5Damage = 30
Tower6Damage = 35

BALLOON_HIT_SOUNDS = {
	"Tower1": "Sound_Tower1.wav",
	"Tower2": "Sound_Tower2.wav",
	"Tower3": "Sound_Tower3.wav",
	"Tower4": "Sound_Tower4.wav",
	"Tower5": "Sound_Tower5.wav",
	"Tower6": "Sound_Tower6.wav"
	}

TIME_PER_SHOT_1 = 500
TIME_PER_SHOT_2 = 500
TIME_PER_SHOT_3 = 500
TIME_PER_SHOT_4 = 500
TIME_PER_SHOT_5 = 500
TIME_PER_SHOT_5 = 500
TIME_PER_SHOT_6 = 500


DIRECTION1X = (743,855)
DIRECTION1Y = (139,160)

DIRECTION2X = (743,855)
DIRECTION2Y = (286,311)

DIRECTION3X = (743,855)
DIRECTION3Y = (459,478)

DIRECTION4X = (874,985)
DIRECTION4Y = (139,160)

DIRECTION5X = (874,985)
DIRECTION5Y = (286,311)

DIRECTION6X = (874,985)
DIRECTION6Y = (459,478)

SAVEBUTTONX = (462,580)
SAVEBUTTONY = (74,124)

