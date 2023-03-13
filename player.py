from settings import *
import pygame as pg

class Player():

    def __init__(self, game):
        self.game = game

        #images
        self.frame_0 = pg.image.load('./Data/Greco/Greco_0.png').convert_alpha()
        self.frame_0 = pg.transform.scale_by(self.frame_0, SCALE_VALUE)
        self.frame_1 = pg.image.load('./Data/Greco/Greco_1.png').convert_alpha()
        self.frame_1 = pg.transform.scale_by(self.frame_1, SCALE_VALUE)
        self.frame_2 = pg.image.load('./Data/Greco/Greco_2.png').convert_alpha()
        self.frame_2 = pg.transform.scale_by(self.frame_2, SCALE_VALUE)
        self.animation = [self.frame_0,self.frame_1,self.frame_2,self.frame_1]
        self.animation_index = 0

        #movement
        self.rect = pg.Rect(WIDTH/2,HEIGHT/2, 15*SCALE_VALUE, 18*SCALE_VALUE)
        self.rect.center = (WIDTH/2,HEIGHT/2)
        
        self.move = self.rect.centery
        self.gravity = 0

        

    def movement(self):

        if self.rect.bottom >= 810: 
            self.rect.bottom = 810
            return None
        
        self.gravity += GRAVITY_FORCE * self.game.deltatime
        self.move += self.gravity * self.game.deltatime
        self.rect.centery = self.move 

    

    def draw(self):
        self.animation_index += ANIMATION_SPEED * self.game.deltatime
        if self.animation_index >=  4: self.animation_index = 0

        if self.animation[int(self.animation_index)] == self.frame_0: self.image_pos = (self.rect.left - 6 * SCALE_VALUE,self.rect.top)
        if self.animation[int(self.animation_index)] == self.frame_1: self.image_pos = (self.rect.left - 8 * SCALE_VALUE,self.rect.top)
        if self.animation[int(self.animation_index)] == self.frame_2: self.image_pos = (self.rect.left - 10 * SCALE_VALUE,self.rect.top)

        if self.gravity < 0: 
            self.game.screen.blit(pg.transform.rotate(self.animation[int(self.animation_index)] , -self.gravity/60),self.image_pos)
        else:
            self.game.screen.blit(pg.transform.rotate(self.animation[int(self.animation_index)], -self.gravity/30),self.image_pos)
        



    def update(self):
        self.movement()
        self.draw()

