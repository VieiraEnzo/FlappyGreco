import pygame as pg
from settings import *

class Pipe():

    def __init__(self, angle, height):
        self.angle = angle
        self.height = height
        self.image = pg.image.load('./Data/Cano.png').convert_alpha()
        self.image = pg.transform.rotate(self.image, angle)
        self.image = pg.transform.scale(self.image, (110,670))
        self.x = WIDTH + 100
        
        if angle == 0:
            self.rect = self.image.get_rect(midtop = (WIDTH + 100, height))
        else:
            
            self.image = pg.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(midbottom = (WIDTH + 100, height - DISTANCIA_CANOS))
    

class Score():
    
    def __init__(self):
        self.move = WIDTH + 100
        self.x = WIDTH + 100 #distancia inicial do cano
        self.score_colided = False


class Ground():

    def __init__(self,x = 0, y = 810):
        self.image = pg.image.load('./Data/chao.png').convert()
        self.x = x
        self.y = y
        self.move = x
    

class Background():

    def __init__(self,x = 0, y = -150):
        self.image = pg.image.load('./Data/Fundo_dia_Grande.png').convert()
        self.image = pg.transform.scale_by(self.image, 5)
        self.x = x
        self.y = y
        self.move = x
