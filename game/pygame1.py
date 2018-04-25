#coding:utf-8
import sys
import pygame
from gamesetting import setting
from gameenity.ship import Ship
from pygame.sprite import Group
from  game import game_function as gf
from  gameenity.alien import Alien
from  game.game_state import Game_State
from gameenity.Button import Button
from game.score_borad import Score_Borad
def run_game():
     pygame.init()
     set=setting.setting()
     screen=pygame.display.set_mode((set.width, set.height))
     state=Game_State(set)
     ship=Ship(screen,set)
     bullets=Group()
     aliens=Group();
     msg="点击开始"
     button=Button(set,screen,msg)
     sb=Score_Borad(screen,set,state)

     pygame.display.set_caption("飞机打外星人")
     gf.create_al(screen, aliens, set)
     while True:
          gf.check_event(ship,bullets,set,screen,state,button)
          gf.update_screen(screen,ship,set,bullets,aliens,state,button,sb)
          gf.check_alines(screen,aliens,set,bullets)



run_game()
