import pygame as pg
from cano import Pipe,Score, Ground, Background
from settings import *
import random


class Obstacles():
    def __init__(self,game):
        self.game = game
        self.obstacles_list = []
        self.points_list = []
        self.ground_list = [Ground(),Ground(x = WIDTH)]
        self.background_list = [Background(),Background(x = WIDTH)]

    	
    
    def append_pipe(self):
        height = random.randint(300,700)
        self.obstacles_list.append(Pipe(0, height))
        self.obstacles_list.append(Pipe(180, height))
        self.points_list.append(Score())
    
    def append_ground(self):
        self.ground_list.append(Ground(x = WIDTH))

    def append_background(self):
        self.background_list.append(Background(x = WIDTH))


    def movement(self):
        for pipe in self.obstacles_list:
            pipe.x -= PIPE_SPEED * self.game.deltatime
            pipe.rect.left = round(pipe.x)

        for point in self.points_list:
            point.move -= PIPE_SPEED * self.game.deltatime
            point.x = round(point.move)
        
        for ground in self.ground_list:
            ground.move -= PIPE_SPEED * self.game.deltatime
            ground.x = ground.move
            if ground.x <= -WIDTH: self.append_ground()

        for background in self.background_list:
            background.move -= BACKGROUND_SPEED * self.game.deltatime
            background.x = background.move
            if background.x <= -WIDTH: self.append_background()




    def draw(self):
        for background in self.background_list:
            self.game.screen.blit(background.image, (background.x, background.y))
        for pipe in self.obstacles_list:
            self.game.screen.blit(pipe.image,pipe.rect)
        for ground in self.ground_list:
            self.game.screen.blit(ground.image, (ground.x, ground.y))

    
    def erase(self):
        self.obstacles_list = [pipe for pipe in self.obstacles_list if pipe.rect.right > -200]
        self.points_list = [point for point in self.points_list if point.x > -200]
        self.ground_list =[ground for ground in self.ground_list if ground.x >= -WIDTH]
        self.background_list =[background for background in self.background_list if background.x >= -WIDTH]
    
    def check_colisions(self):

        for pipe in self.obstacles_list:
            if self.game.player.rect.colliderect(pipe.rect):
              return False

        for point in self.points_list:
            if point.x <= WIDTH/2 and not point.score_colided:
                self.game.score += 1
                point.score_colided = True

                
        if self.game.player.rect.bottom >= 810:
            return False

        if self.game.player.rect.top <= 0:
            return False

        return True
    
    

    def update(self):
        self.movement()
        self.erase()
        self.draw()
