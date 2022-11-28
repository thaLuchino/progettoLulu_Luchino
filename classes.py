import pygame
import constants as CONST
import math
import os
from game import *

screen = pygame.display.set_mode(((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT)))


class position():

    def __init__(self, x = 100, y = 100):
        self.x = x
        self.y = y

    def distance(self, p):
        self.distance = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

class Object_in_Game():

    def __init__(self, p = position(), health = 100, player = 0):
        self.position = p
        self.health = health 
        self.image = pygame.image.load('placeholder.png')
        self.player = player
        self.direction = 1
        self.frame = 0
        

    #def create_images(self, image = (('placeholder.png'))):
       # i = pygame.image.load(image)
        #screen.blit(i, ((self.position.x-(i.get_width()/2),self.position.y-(i.get_height()))))



class Building(Object_in_Game):
     def __init__(self,p=position(), player = 0):
        super().__init__(p , player)
    

class Mines(Building):
    def __init__(self, p=position(), player = 0):
        super().__init__(p, player)
        self.p = position()
        self.player = player
        if self.player == 1:
            self.image = pygame.image.load('sprites/player1/building/mine.png')   #si potrebbe creare una funzione che per ogni building fa questa distinzione tra player 1 e 2
        elif self.player == 2:
            self.image = pygame.image.load('sprites/player2/building/mine.png')
        else:
            self.image = None
        #super().create_images(self, image =(('sprites/player1/building/mine.png')))

class Barracks(Building):
    def __init__(self, p=position(), player = 0):
        super().__init__(p, player)
        self.player = player
        if self.player ==1:
            self.image = pygame.image.load('sprites/player1/building/barracks.png')
        elif self.player == 2:
            self.image = pygame.image.load('sprites/player2/building/barracks.png')
        else:
            self.image = None


class Towers(Building):
    def __init__(self, p=position(), player = 0):
        super().__init__(p, player)
        self.player = player
        if self.player ==1:
            self.image = pygame.image.load('sprites/player1/building/tower.png')
        elif self.player == 2:
            self.image = pygame.image.load('sprites/player2/building/tower.png')
        else:
            self.image = None

class Walls(Building):
    def __init__(self, p=position(), player = 0):
        super().__init__(p, player)
        self.player = player
        if self.player ==1:
            self.image = pygame.image.load('sprites/player1/building/wall.png')
        elif self.player == 2:
            self.image = pygame.image.load('sprites/player2/building/wall.png')
        else:
            self.image = None















        

        

        
    
            





        



    








