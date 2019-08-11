"""
main.py
File puts everything together and runs the main core of the game
"""

# Format and framework from: KidsCanCode - Game Development with pygame video series

import pygame
import sys
import random
import math
from random import uniform
from os import path
from settings import *
from Towers import *
from Enemy import *
from Bullet import *

#directory where images are located
img_dir = path.join(path.dirname(__file__), '')

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.money = 600
        self.lives = 50
        self.startWave = False
        self.gameMode = None
        self.selection = (-1,-1)
        self.current = 2
        self.oneRunThrough = True
        self.currentLevel = 0
        self.levelOver = False
        self.balloonStren = 3
        
        self.selectedTower = None
        self.gameOver = False
        self.damage = 0
        self.soundType = None
        
        self.highscore = 0
        self.tower1Grid = False
        self.tower2Grid = False
        self.tower3Grid = False
        self.tower4Grid = False
        self.tower5Grid = False
        self.tower6Grid = False

        self.direction1 = 0
        self.direction2 = 0
        self.direction3 = 0
        self.direction4 = 0
        self.direction5 = 0
        self.direction6 = 0

        self.speedYELLOW = 15
        self.speedBLUE = 12
        self.speedPURPLE = 8
        self.speedRED = 5
        self.speedMOAB = 3

        self.time1 = TIME_PER_SHOT_1
        self.time2 = TIME_PER_SHOT_2
        self.time3 = TIME_PER_SHOT_3
        self.time4 = TIME_PER_SHOT_4
        self.time5 = TIME_PER_SHOT_5
        self.time6 = TIME_PER_SHOT_6

        self.upgraded1 = False
        self.upgraded2 = False
        self.upgraded3 = False
        self.upgraded4 = False
        self.upgraded5 = False
        self.upgraded6 = False

        self.nonLegalVals = []
        self.nonLegalCols = [12,13,14,15]
        self.legalRows = [10,11]

        self.selectedCoords =[]
        self.doneCreating = False
        self.createButtonCoords = [(9,0),(9,1),(9,2),(9,3)]
        self.savePressed = False

        self.dir = path.dirname(__file__)
        self.font_name = pygame.font.match_font(FONT_NAME)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):

        #load all images
        #convert_alpha gets rid of whitespace surrounding the "png" images
        #toweer images
        game_folder = path.dirname(__file__)
        self.imageT1 = pygame.image.load(path.join('', "tower1.png")).convert_alpha()
        self.imageT1 = pygame.transform.scale(self.imageT1, (70,70))        #scales the image to fit on the screen
        self.imageT2 = pygame.image.load(path.join('', "tower2.png")).convert_alpha()
        self.imageT2 = pygame.transform.scale(self.imageT2, (70,70))
        self.imageT3 = pygame.image.load(path.join('', "tower3.png")).convert_alpha()
        self.imageT3 = pygame.transform.scale(self.imageT3, (70,70))
        self.imageT4 = pygame.image.load(path.join('', "tower4.png")).convert_alpha()
        self.imageT4 = pygame.transform.scale(self.imageT4, (70,70))
        self.imageT5 = pygame.image.load(path.join('', "tower5.png")).convert_alpha()
        self.imageT5 = pygame.transform.scale(self.imageT5, (70,70))
        self.imageT6 = pygame.image.load(path.join('', "tower6.png")).convert_alpha()
        self.imageT6 = pygame.transform.scale(self.imageT6, (70,70))

        #balloon/ enemy images
        self.balloon_red = pygame.image.load(path.join('', "balloon_red.png")).convert_alpha()
        self.balloon_red = pygame.transform.scale(self.balloon_red, (40,70))
        self.balloon_purple = pygame.image.load(path.join('', "balloon_purple.png")).convert_alpha()
        self.balloon_purple = pygame.transform.scale(self.balloon_purple, (40,70))
        self.balloon_blue = pygame.image.load(path.join('', "balloon_blue.png")).convert_alpha()
        self.balloon_blue = pygame.transform.scale(self.balloon_blue, (40,70))
        self.balloon_yellow = pygame.image.load(path.join('', "balloon_yellow.png")).convert_alpha()
        self.balloon_yellow = pygame.transform.scale(self.balloon_yellow, (40,70))
        self.balloon_moab = pygame.image.load(path.join('', "balloon_moab.png")).convert_alpha()
        self.balloon_moab = pygame.transform.scale(self.balloon_moab, (60,30))
        self.balloon_moab = pygame.transform.rotate(self.balloon_moab,180)      #rotate the image for horizontally

        #background images
        self.background = pygame.image.load(path.join(img_dir, "background.jpg")).convert()
        self.background_rect = self.background.get_rect()
        self.background_medium = pygame.image.load(path.join(img_dir, "background_medium.jpeg")).convert()
        self.background_medium = pygame.transform.scale(self.background_medium, (1280,800))
        self.background_medium_rect = self.background_medium.get_rect()
        self.background_hard = pygame.image.load(path.join(img_dir, "background_hard.jpeg")).convert()
        self.background_hard = pygame.transform.scale(self.background_hard, (1180,770))
        self.background_hard_rect = self.background_hard.get_rect()

        #bullet images
        self.bullet_basketball = pygame.image.load(path.join(img_dir, "bullet_basketball.png")).convert_alpha()
        self.bullet_basketball = pygame.transform.scale(self.bullet_basketball, (30,30))
        self.bullet_soccer = pygame.image.load(path.join(img_dir, "bullet_soccer.png")).convert_alpha()
        self.bullet_soccer = pygame.transform.scale(self.bullet_soccer, (30,30))
        self.bullet_golf = pygame.image.load(path.join(img_dir, "bullet_golf.png")).convert_alpha()
        self.bullet_golf = pygame.transform.scale(self.bullet_golf, (30,20))
        self.bullet_tennis = pygame.image.load(path.join(img_dir, "bullet_tennis.png")).convert_alpha()
        self.bullet_tennis = pygame.transform.scale(self.bullet_tennis, (25,25))
        self.bullet_volley = pygame.image.load(path.join(img_dir, "bullet_volley.png")).convert_alpha()
        self.bullet_volley = pygame.transform.scale(self.bullet_volley, (25,25))
        self.bullet_football = pygame.image.load(path.join(img_dir, "bullet_football.png")).convert_alpha()
        self.bullet_football = pygame.transform.scale(self.bullet_football, (15,30))
        self.bullet_football = pygame.transform.rotate(self.bullet_football,90)

        #learned how to use sound and files from KIDSCANCODE Tutorial
        #load background music
        pygame.mixer.music.load(path.join('', "background_music.ogg"))
        self.balloon_hit_sounds = {}
        for type in BALLOON_HIT_SOUNDS:
            self.balloon_hit_sounds[type] = pygame.mixer.Sound(path.join('', BALLOON_HIT_SOUNDS[type]))

        #choose map based on game mode
        self.map_data = []
        if(self.gameMode == "Easy"):
            self.lives = 50
            self.money = 1000
            self.strMap = "map.txt"
        elif(self.gameMode == "Medium"):
            self.lives = 40
            self.money = 900
            self.strMap = "map2.txt"
        elif(self.gameMode == "Hard"):
            self.lives = 30
            self.money = 800
            self.strMap = "map3.txt"
        else:
            self.strMap = "map.txt"

        #get input from txt files of how the map should look
        with open(path.join(game_folder, self.strMap), 'rt') as f:
            for line in f:
                self.map_data.append(line)

        #load high score,lives,gameMode if it exists from file, else set to default
        with open(path.join(game_folder, "Score.txt"), 'rt') as f:
            try:
                self.highscore = int(f.readline())
                self.lives = int(f.readline())
                self.gameMode = str(f.readLine())
            except:
                self.highscore = 0

    def new(self):
        # initialize all variables and do all the setup for a new game
        # Balloon type differs based on difficulty of game
        if(self.gameMode == "Easy"):
            self.balloonStren = 3
        elif(self.gameMode == "Medium"):
            self.balloonStren = 4
        elif(self.gameMode == "Hard"):
            self.balloonStren = 5
        #create sprite groups for all types of sprites
        self.all_sprites = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        if(self.gameMode!="Create"):
            for row, tiles in enumerate(self.map_data):
                for col, tile in enumerate(tiles):
                    if tile == '1':
                        Wall(self, col, row)
                        self.nonLegalVals.append((row,col))
        self.enemy = pygame.sprite.Group()
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        #play music indefinitely 
        pygame.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

        if(self.gameMode != "Create"):
            #if start button pressed, load the balloons
            if(self.startWave==True):
                #if current level is not over
                if(self.levelOver==False):
                    if(len(str(pygame.time.get_ticks()))==4):       #timer for different levels
                        new = int(str(pygame.time.get_ticks())[0])
                    elif(len(str(pygame.time.get_ticks()))==5):
                        new = int(str(pygame.time.get_ticks())[0:2])
                    else:
                        new = int(str(pygame.time.get_ticks())[0:3])
                    if(self.currentLevel==1):
                        if(new>=LEVEL1TIME):
                            self.levelOver = True       #set levelOver to true if time exceeds level 1 time
                    if(self.currentLevel==2):
                        if(new>=LEVEL2TIME):
                            self.levelOver = True
                    if(self.currentLevel==3):
                        if(new>=LEVEL3TIME):
                            self.levelOver = True
                    if(self.currentLevel==4):
                        if(new>=LEVEL4TIME):
                            self.levelOver = True
                    if(self.currentLevel>=5):
                        if(new>=LEVEL5TIME):            #set GameOver if user completes all five levels
                            self.levelOver = True
                            if(new>=GAMEOVERTIME):
                                self.startWave = False
                                self.gameOver = True
                    if(new-self.current >= 1):          #add a balloon to the screen every second(ish)
                        self.m = Enemy(self)
                        self.all_sprites.add(self.m)
                        self.enemy.add(self.m)
                        self.current = new

        #AI COMPONENT
        #check to see if tower1/tower2 upgraded and move balloons faster
        if(self.upgraded1 or self.upgraded2):
            self.speedPURPLE = 11
            self.speedRED = 8

        #adjust speed of ballon if higher towers are upgraded
        if(self.upgraded3):
            self.balloonStren = 3
            self.speedPURPLE = 11
            self.speedYELLOW = 16

        if(self.upgraded5 or self.upgraded4):
            self.balloonStren = 4
            self.speedYELLOW = 17
            self.speedBLUE = 15

        if(self.upgraded6):
            self.balloonStren = 4
            self.speedRED = 10
            self.speedBLUE = 17

        #if tower 5 and 6 upgraded, make game difficult by placing only MOABS
        if(self.upgraded6 and self.upgraded5):
            self.balloonStren = 5
            self.speedMOAB = 5

        if(self.gameMode == "Easy"):
            if(self.money<10 and self.lives < 10):
                self.speedPURPLE = 8
                self.speedYELLOW = 13
            if(self.money>1000 and self.lives > 10):
                self.balloonStren = 4
                self.speedPURPLE = 13
        if(self.gameMode == "Medium"):
            if(self.money<10 and self.lives<10):
                self.speedYELLOW = 19
                self.speedBLUE = 14
            if(self.money > 1000 and self.lives > 10):
                self.balloonStren = 5
        if(self.gameMode == "Hard"):
            if(self.money<10 and self.lives < 10):
                self.speedRED = 10
            if(self.money > 1000 and self.lives > 10):
                self.balloonStren = 5

        if(self.lives<=0):
            self.gameOver = True
        if(self.gameOver):
            self.show_go_screen()

        #check for collisions between bullets and balloons and decrease health if collision takes place
        hits = pygame.sprite.groupcollide(self.enemy, self.bullets, False, True)
        for hit in hits:
            #play music based on what tower hit the balloon
            self.balloon_hit_sounds[self.soundType].play()
            self.money+=MONEYBALLOONHIT         #money per balloon hit
            hit.health-=self.damage

    def draw_grid(self):
        #Draw the grid of the game
        if(self.gameMode!="Create"):
            for x in range(0, WIDTH, TILESIZE):
                pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, TILESIZE):
                pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        #if create own level mode, user can click where they want to place walls 
        if(self.gameMode == "Create"):
            for row in range(0, ROWS):
                for col in range(0, COLS):
                    (x0, y0, x1, y1) = self.getCellBounds(row, col)
                    #ensure wall in constraints
                    if ((row,col) in self.selectedCoords and (col not in self.nonLegalCols or row in self.legalRows) and (row,col) not in self.createButtonCoords):
                        Wall(self, col, row)

    #draw all images and texts as necessary
    def draw(self):
        #draw background picture
        if(self.gameMode=="Easy"):
            self.screen.fill(BLACK)
            self.screen.blit(self.background, self.background_rect)
        elif(self.gameMode=="Medium"):
            self.screen.fill(BLACK)
            self.screen.blit(self.background_medium, self.background_medium_rect)
        elif(self.gameMode == "Hard"):
            self.screen.fill(BLACK)
            self.screen.blit(self.background_hard, self.background_hard_rect)
        elif(self.gameMode == "Create"):
            self.screen.fill(MAROON)
        self.draw_grid()
        #No level should be on screen during create mode
        if(self.gameMode!="Create"):
            self.draw_text("Level: " + str(self.currentLevel), 48, WHITE, 350, 140)
        if(self.gameMode == "Create"):
            self.draw_text("Done Creating", 48, WHITE, 160,580)

        #Draw the text that appears on the screen
        self.draw_text("BLOONS TOWER DEFENSE", 48, WHITE, 400, 20)
        self.draw_text("Mode: " + self.gameMode, 48, WHITE, 280, 80)
        self.draw_text("SAVE",48, WHITE, 520, 80)
        self.draw_text("MONEY: $" + str(int(self.money)), 48, WHITE, 860, 20)
        self.draw_text("LIVES: " + str(int(math.floor(self.lives))), 48, WHITE, 860, 80)
        self.draw_text("START ", 48, WHITE, 880, 600)

        #tower helper - displays the description for the tower
        pygame.draw.rect(self.screen,AQUA,(0,640,320,800))
        self.draw_text("TOWER HELPER", 30, BLACK, 160,650)
        self.draw_text("Selected Tower: " + str(self.selectedTower), 24, BLACK, 100,690)
        self.draw_text("Description: " + towerTypes[str(self.selectedTower)]["description"],24,BLACK,125,720)
        self.draw_text("Price: $" + str(towerTypes[str(self.selectedTower)]["price"]),24,BLACK,125,750)

        #Draw direction button above each tower
        self.draw_text("DIRECTION",30,WHITE,800,140)
        self.draw_text("DIRECTION",30,WHITE,800,290)
        self.draw_text("DIRECTION",30,WHITE,800,460)
        self.draw_text("DIRECTION",30,WHITE,930,140)
        self.draw_text("DIRECTION",30,WHITE,930,290)
        self.draw_text("DIRECTION",30,WHITE,930,460)

        #Draw upgrade/upgraded beneath each tower
        if(self.upgraded1): 
            self.draw_text("UPGRADED",30,RED,800,240)
        else:   
            self.draw_text("UPGRADE",30,WHITE,800,240)
        if(self.upgraded2): 
            self.draw_text("UPGRADED",30,RED,800,400)
        else:   
            self.draw_text("UPGRADE",30,WHITE,800,400)
        if(self.upgraded3): 
            self.draw_text("UPGRADED",30,RED,800,555)
        else:   
            self.draw_text("UPGRADE",30,WHITE,800,555)
        if(self.upgraded4): 
            self.draw_text("UPGRADED",30,RED,930,240)
        else:   
            self.draw_text("UPGRADE",30,WHITE,930,240)
        if(self.upgraded5): 
            self.draw_text("UPGRADED",30,RED,930,400)
        else:   
            self.draw_text("UPGRADE",30,WHITE,930,400)
        if(self.upgraded6): 
            self.draw_text("UPGRADED",30,RED,930,555)
        else: 
            self.draw_text("UPGRADE",30,WHITE,930,555)
        
        #draw the tower buttons on the side of the screen
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.screen.blit(self.imageT1,(769,259))
                if tile == '2':
                    self.screen.blit(self.imageT1,(769,160))
                if tile == '3':
                    self.screen.blit(self.imageT2,(769,311))
                if tile == '4':
                    self.screen.blit(self.imageT3,(769,480))
                if tile == '5':
                    self.screen.blit(self.imageT4,(896,160))
                if tile == '6':
                    self.screen.blit(self.imageT5,(896,311))
                if tile == '7':
                    self.screen.blit(self.imageT6,(896,480))
        
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        # catch all events here

        #if mode is not in create (actual game mode)
        if(self.gameMode != "Create"):
            for event in pygame.event.get():

                #left click to select tower
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    (x, y) = (event.pos)

                    #startButton
                    if x>StartButX[0] and x<StartButX[1] and y>StartButY[0] and y<StartButY[1]:
                        self.startWave = True
                        self.currentLevel+=1
                        if(self.currentLevel>5):
                            self.currentLevel = 5
                        #print(self.currentLevel)
                        self.levelOver = False

                    #check to see if any tower button pressed
                    if x>Tower1X[0] and x<Tower1X[1] and y>Tower1Y[0] and y<Tower1Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower1"
                    if x>Tower2X[0] and x<Tower2X[1] and y>Tower2Y[0] and y<Tower2Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower2"
                    if x>Tower3X[0] and x<Tower3X[1] and y>Tower3Y[0] and y<Tower3Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower3"
                    if x>Tower4X[0] and x<Tower4X[1] and y>Tower4Y[0] and y<Tower4Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower4"
                    if x>Tower5X[0] and x<Tower5X[1] and y>Tower5Y[0] and y<Tower5Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower5"
                    if x>Tower6X[0] and x<Tower6X[1] and y>Tower6Y[0] and y<Tower6Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower6"
                    
                    #check to see if upgrade button pressed only if the tower is already on the screen
                    if x>UPGRADE1X[0] and x<UPGRADE1X[1] and y>UPGRADE1Y[0] and y<UPGRADE1Y[1]:
                        if(self.tower1Grid and (self.money-TOWER1PRICE/2)>=0):
                            self.time1 = 300
                            self.money-=TOWER1PRICE/2           #Decrease the amount of money if upgraded is clicked
                            self.upgraded1 = True
                    if x>UPGRADE2X[0] and x<UPGRADE2X[1] and y>UPGRADE2Y[0] and y<UPGRADE2Y[1]:
                        if(self.tower2Grid and (self.money-TOWER2PRICE/2)>=0):
                            self.time2 = 280
                            self.money-=TOWER2PRICE/2
                            self.upgraded2 = True
                    if x>UPGRADE3X[0] and x<UPGRADE3X[1] and y>UPGRADE3Y[0] and y<UPGRADE3Y[1]:
                        if(self.tower3Grid and (self.money-TOWER3PRICE/2)>=0):
                            self.time3 = 260
                            self.money-=TOWER3PRICE/2
                            self.upgraded3 = True
                    if x>UPGRADE4X[0] and x<UPGRADE4X[1] and y>UPGRADE4Y[0] and y<UPGRADE4Y[1]:
                        if(self.tower4Grid and (self.money-TOWER4PRICE/2)>=0):
                            self.time4 = 240
                            self.money-=TOWER4PRICE/2
                            self.upgraded4 = True
                    if x>UPGRADE5X[0] and x<UPGRADE5X[1] and y>UPGRADE5Y[0] and y<UPGRADE5Y[1]:
                        if(self.tower5Grid and (self.money-TOWER5PRICE/2)>=0):
                            self.time5 = 230
                            self.money-=TOWER5PRICE/2
                            self.upgraded5 = True
                    if x>UPGRADE6X[0] and x<UPGRADE6X[1] and y>UPGRADE6Y[0] and y<UPGRADE6Y[1]:
                        if(self.tower6Grid and (self.money-TOWER6PRICE/2)>=0):
                            self.time6 = 220
                            self.money-=TOWER6PRICE/2
                            self.upgraded6 = True

                    #if the save button pressed, save the money, lives, and gamemode into the Score.txt file
                    if x>SAVEBUTTONX[0] and x<SAVEBUTTONX[1] and y>SAVEBUTTONY[0] and y<SAVEBUTTONY[1]:
                        self.savePressed = True
                        if self.money > self.highscore:
                            self.highscore = self.money
                            with open(path.join(self.dir, "Score.txt"), 'w') as f:
                                f.write(str(self.money))
                                f.write("\n")
                                if(self.savePressed):
                                    f.write(str(abs(self.lives)))
                                    f.write("\n")
                                    f.write(str(self.gameMode))

                #right click to place tower
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    (x, y) = (event.pos)
                    (row, col) = self.getCell(x, y)
                    #check to see if if start button clicked and if placing the tower is legal 
                    #also check to see if enough money to place tower
                    if(self.startWave and self.selectedTower!=None):
                        if(self.selectedTower == "Tower1" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER1PRICE>=0):
                                self.money -= TOWER1PRICE
                                self.tower1Grid = True    #set to true to check during AI portion of code
                                self.tower1 = Tower1(self,RED,col,row)
                                self.towers.add(self.tower1)
                        if(self.selectedTower == "Tower2" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER2PRICE>=0):
                                self.money -= TOWER2PRICE
                                self.tower2Grid = True
                                self.tower2 = Tower2(self,RED,col,row)
                                self.towers.add(self.tower2)
                        if(self.selectedTower == "Tower3" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER3PRICE>=0):
                                self.money -= TOWER3PRICE
                                self.tower3Grid = True
                                self.tower3 = Tower3(self,RED,col,row)
                                self.towers.add(self.tower3)
                        if(self.selectedTower == "Tower4" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER4PRICE>=0):
                                self.money -= TOWER4PRICE
                                self.tower4Grid = True
                                self.tower4 = Tower4(self,RED,col,row)
                                self.towers.add(self.tower4)
                        if(self.selectedTower == "Tower5" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER5PRICE>=0):
                                self.money -= TOWER5PRICE
                                self.tower5Grid = True
                                self.tower5 = Tower5(self,RED,col,row)
                                self.towers.add(self.tower5)
                        if(self.selectedTower == "Tower6" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER6PRICE>=0):
                                self.money -= TOWER6PRICE
                                self.tower6Grid = True
                                self.tower6 = Tower6(self,RED,col,row)
                                self.towers.add(self.tower6)

                #if the direction button is pressed, change the direction of shooting
                #scroll up
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                    (x,y) = event.pos

                    if x>DIRECTION1X[0] and x<DIRECTION1X[1] and y>DIRECTION1Y[0] and y<DIRECTION1Y[1]:
                        self.direction1+=1
                    if x>DIRECTION2X[0] and x<DIRECTION2X[1] and y>DIRECTION2Y[0] and y<DIRECTION2Y[1]:
                        self.direction2+=1
                    if x>DIRECTION3X[0] and x<DIRECTION3X[1] and y>DIRECTION3Y[0] and y<DIRECTION3Y[1]:
                        self.direction3+=1
                    if x>DIRECTION4X[0] and x<DIRECTION4X[1] and y>DIRECTION4Y[0] and y<DIRECTION4Y[1]:
                        self.direction4+=1
                    if x>DIRECTION5X[0] and x<DIRECTION5X[1] and y>DIRECTION5Y[0] and y<DIRECTION5Y[1]:
                        self.direction5+=1
                    if x>DIRECTION6X[0] and x<DIRECTION6X[1] and y>DIRECTION6Y[0] and y<DIRECTION6Y[1]:
                        self.direction6+=1

                #if the direction button is pressed, change the direction of shooting
                #scroll down
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                    (x,y) = event.pos

                    if x>DIRECTION1X[0] and x<DIRECTION1X[1] and y>DIRECTION1Y[0] and y<DIRECTION1Y[1]:
                        self.direction1-=1
                    if x>DIRECTION2X[0] and x<DIRECTION2X[1] and y>DIRECTION2Y[0] and y<DIRECTION2Y[1]:
                        self.direction2-=1
                    if x>DIRECTION3X[0] and x<DIRECTION3X[1] and y>DIRECTION3Y[0] and y<DIRECTION3Y[1]:
                        self.direction3-=1
                    if x>DIRECTION4X[0] and x<DIRECTION4X[1] and y>DIRECTION4Y[0] and y<DIRECTION4Y[1]:
                        self.direction4-=1
                    if x>DIRECTION5X[0] and x<DIRECTION5X[1] and y>DIRECTION5Y[0] and y<DIRECTION5Y[1]:
                        self.direction5-=1
                    if x>DIRECTION6X[0] and x<DIRECTION6X[1] and y>DIRECTION6Y[0] and y<DIRECTION6Y[1]:
                        self.direction6-=1

                #if user clicks exit, then exit the game
                if event.type == pygame.QUIT:
                    self.quit()
                    if self.playing:
                        self.playing = False
                    self.running = False

        #if in create mode, run until the done creating button is pressed
        if(self.gameMode == "Create"):
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    (x, y) = (event.pos)
                    (row,col) = self.getCell(x,y)

                    if x>Tower1X[0] and x<Tower1X[1] and y>Tower1Y[0] and y<Tower1Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower1"
                    if x>Tower2X[0] and x<Tower2X[1] and y>Tower2Y[0] and y<Tower2Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower2"
                    if x>Tower3X[0] and x<Tower3X[1] and y>Tower3Y[0] and y<Tower3Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower3"
                    if x>Tower4X[0] and x<Tower4X[1] and y>Tower4Y[0] and y<Tower4Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower4"
                    if x>Tower5X[0] and x<Tower5X[1] and y>Tower5Y[0] and y<Tower5Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower5"
                    if x>Tower6X[0] and x<Tower6X[1] and y>Tower6Y[0] and y<Tower6Y[1]:
                        if(self.startWave):
                            self.selectedTower = "Tower6"

                    #add (row,col) to selected coordinates list to make new map
                    self.selectedCoords.append((row,col))

                    if x>CREATINGBUTTONX[0] and x<CREATINGBUTTONX[1] and y>CREATINGBUTTONY[0] and y<CREATINGBUTTONY[1]:
                        self.doneCreating = True

                    #if done creating button clicked, add it to the file Create.txt
                    if(self.doneCreating):
                        with open(path.join(self.dir, "Create.txt"), 'w') as f:
                            f.write(str(self.selectedCoords))
                            #self.doneCreating = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    (x, y) = (event.pos)
                    (row, col) = self.getCell(x, y)
                    #check to see if if start button clicked and if placing the tower is legal 
                    #also check to see if enough money to place tower
                    if(self.startWave and self.selectedTower!=None):
                        if(self.selectedTower == "Tower1" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER1PRICE>=0):
                                self.money -= TOWER1PRICE
                                self.tower1Grid = True    #set to true to check during AI portion of code
                                self.tower1 = Tower1(self,RED,col,row)
                                self.towers.add(self.tower1)
                        if(self.selectedTower == "Tower2" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER2PRICE>=0):
                                self.money -= TOWER2PRICE
                                self.tower2Grid = True
                                self.tower2 = Tower2(self,RED,col,row)
                                self.towers.add(self.tower2)
                        if(self.selectedTower == "Tower3" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER3PRICE>=0):
                                self.money -= TOWER3PRICE
                                self.tower3Grid = True
                                self.tower3 = Tower3(self,RED,col,row)
                                self.towers.add(self.tower3)
                        if(self.selectedTower == "Tower4" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER4PRICE>=0):
                                self.money -= TOWER4PRICE
                                self.tower4Grid = True
                                self.tower4 = Tower4(self,RED,col,row)
                                self.towers.add(self.tower4)
                        if(self.selectedTower == "Tower5" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER5PRICE>=0):
                                self.money -= TOWER5PRICE
                                self.tower5Grid = True
                                self.tower5 = Tower5(self,RED,col,row)
                                self.towers.add(self.tower5)
                        if(self.selectedTower == "Tower6" and (row,col) not in self.nonLegalVals and \
                            (col not in self.nonLegalCols or row in self.legalRows)):
                            if(self.money-TOWER6PRICE>=0):
                                self.money -= TOWER6PRICE
                                self.tower6Grid = True
                                self.tower6 = Tower6(self,RED,col,row)
                                self.towers.add(self.tower6)

                # check for closing window
                if event.type == pygame.QUIT:
                    self.quit()
                    if self.playing:
                        self.playing = False
                    self.running = False

    #FROM THE 112 Website (https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html)
    def getCell(self,x, y):
        # aka "viewToModel"
        # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
        if (not self.pointInGrid(x, y)):
            return (-1, -1)
        gridWidth  = WIDTH 
        gridHeight = HEIGHT
        cellWidth  = WIDTH//COLS
        cellHeight = HEIGHT//ROWS
        row = y // cellHeight
        col = x // cellWidth
        # triple-check that we are in bounds
        row = min(ROWS-1, max(0, row))
        col = min(COLS-1, max(0, col))
        return (row, col)

    #FROM THE 112 Website (https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html)
    def pointInGrid(self,x, y):
    # return True if (x, y) is inside the grid defined by data.
        return ((x <= WIDTH) and
                (y <= HEIGHT))

    #FROM THE 112 Website (https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html)
    def getCellBounds(self,row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
        gridWidth  = WIDTH 
        gridHeight = HEIGHT
        columnWidth = WIDTH//COLS
        rowHeight = HEIGHT//ROWS
        x0 = col * columnWidth
        x1 = (col+1) * columnWidth
        y0 = row * rowHeight
        y1 = (row+1) * rowHeight
        return (x0, y0, x1, y1)

    #display the start screen with intructions how to play and prompt the user which game mode they want to play in
    def show_start_screen(self):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("BEAT THE ENEMIES", 22, WHITE, WIDTH / 2, HEIGHT / 2.8)
        self.draw_text("Intructions:", 22, WHITE, WIDTH/2, HEIGHT/2.4)
        self.draw_text("CURRENT HIGH SCORE: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 1.7)
        self.draw_text("Click on tower to select, Right Click to place, Scroll to change Direction, Start to begin new level", 22, WHITE, WIDTH/2, HEIGHT/2.2)
        self.draw_text("Easy", 22, WHITE, WIDTH / 5, HEIGHT * 3 / 4)
        self.draw_text("Medium", 22, WHITE, 2*WIDTH / 5, HEIGHT * 3 / 4)
        self.draw_text("Hard", 22, WHITE, 3*WIDTH/5, HEIGHT * 3 / 4)
        self.draw_text("Create", 22, WHITE, 4*WIDTH/5, HEIGHT * 3 / 4)
        pygame.display.flip()

        #user select game mdoe
        if(x<WIDTH/4):
            self.gameMode = "Easy"
        elif(x>WIDTH/4 and x<2*WIDTH/4):
            self.gameMode = "Medium"
        elif(x>2*WIDTH/4 and x<3*WIDTH/4):
            self.gameMode = "Hard"
        else:
            self.gameMode = "Create"

        self.load_data()
        self.wait_for_key()
    
    #DRAW TEXT FUNCTION FROM THE KIDSCANCODE TUTORIAL
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    #show the final screen once the game is over
    def show_go_screen(self):

        if not self.playing:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Click anywhere to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        #check if new highscore
        if self.money > self.highscore:
            self.highscore = self.money
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            #place contents into file only if new high score is reached
            with open(path.join(self.dir, "Score.txt"), 'w') as f:
                f.write(str(self.money))
                f.write("\n")
                if(self.savePressed):
                    f.write(str(math.abs(self.lives)))
                    f.write("\n")
                    f.write(str(self.gameMode))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pygame.display.flip()
        self.wait_for_key()

    #WAIT FOR KEY FUNCTION FROM THE KIDSCANCODE TUTORIAL
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
