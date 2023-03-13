from settings import *
import pygame as pg
import sys
from player import Player
from obstacles import Obstacles
from pygame import mixer
import time
import random



class Game():
    
    def __init__(self):
        pg.init()
        pg.display.set_caption('Flappy Greco')
        self.game_active = False

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.deltatime = 1


        self.obstacle_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.obstacle_timer, PIPE_FREQUENCY)

        self.score_font = pg.font.Font('./Data/font/score.TTF',50)
        self.title_font = pg.font.Font('./Data/font/score.TTF',52)
        self.control_font = pg.font.Font('./Data/font/score.TTF',22)

        self.menu = pg.image.load('./Data/Menu.png').convert()

        self.audio_10_sound = pg.mixer.Sound(EVERY_10_AUDIO)
        self.audio_die =pg.mixer.Sound(AUDIO_DIE)
        self.audio_point =pg.mixer.Sound(AUDIO_POINT)
        self.audio_jump =pg.mixer.Sound(AUDIO_JUMP)

        self.greco_audio_1 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_1.wav')
        self.greco_audio_2 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_2.wav')
        self.greco_audio_3 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_3.wav')
        self.greco_audio_4 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_4.wav')
        self.greco_audio_5 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_5.wav')
        self.greco_audio_6 = pg.mixer.Sound('./Sounds/Audio_Greco_Start_6.wav')
        self.greco_audio_list = [self.greco_audio_1,self.greco_audio_2,self.greco_audio_3,self.greco_audio_4,self.greco_audio_5,self.greco_audio_6]

        self.score = 0
        self.previus_score = 0
        self.can_start_new_game =False

    
    def update(self):
        pg.display.update()
        self.deltatime = self.clock.tick() /1000

    def check_event(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if self.game_active:

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: 
                        self.player.gravity = JUMP_FORCE
                        self.audio_jump.play()
        

                if event.type == self.obstacle_timer: self.obstacles.append_pipe()

            if self.can_start_new_game:
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE: self.new_game()

            if not self.game_active and not self.can_start_new_game:
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE: self.run_menu()

    def new_game(self):
        self.can_start_new_game = False
        self.score = 0
        self.previus_score = 0
        self.game_active = True
        self.player = Player(self)
        self.obstacles = Obstacles(self)
        self.run()
        self.run_menu()

    def run_menu(self):
        self.can_start_new_game = True
        while not self.game_active:
            self.screen.blit(self.menu, (0,0))
            self.check_event()
            self.draw_menu()
            self.draw_controls()
            self.update()
            
    def draw_controls(self):
        control_draw = self.control_font.render('- Press Space to start -', False, 'Black')
        self.screen.blit(control_draw,control_draw.get_rect(center = (WIDTH/2,90)))

    def draw_score(self):
        score_draw = self.score_font.render(str(self.score), False, '0xf1e335')
        self.screen.blit(score_draw,score_draw.get_rect(center = (WIDTH/2,60)))
    
    def draw_menu(self):
        score_draw = self.title_font.render('Flappy Greco', False, 'Black')
        self.screen.blit(score_draw,score_draw.get_rect(center = (WIDTH/2,60)))
          
    def play_sounds(self):
        if self.score % 10 == 0 and self.previus_score != self.score: 
            self.audio_10_sound.play()
            
        elif self.score %1 == 0 and self.previus_score != self.score:
            self.audio_point.play()
        
        self.previus_score = self.score
        
    
    
    def run(self):

        self.audio_init_game = self.greco_audio_list[random.randint(0,5)]
        self.audio_init_game.play()

        while self.game_active:
            self.check_event()
            self.update()
            self.obstacles.update()
            self.player.update()
            self.draw_score()
            self.game_active = self.obstacles.check_colisions()
            self.play_sounds()
        

            if SHOW_HITBOXES :
                pg.draw.rect(self.screen,(0,255,0), self.player.rect,4)
                for pipe in self.obstacles.obstacles_list:
                    pg.draw.rect(self.screen,(255,0,0), pipe.rect,4)

        self.audio_die.play()
        time_died = time.time()

        while time.time() - time_died < 2:
            self.check_event()
            self.update()
            self.obstacles.draw()
            self.player.animation_index = 0
            self.player.update()
            self.draw_score()
            self.obstacles.check_colisions()
            
            
            
             
            
if __name__ == '__main__':
    game = Game()
    game.run_menu()