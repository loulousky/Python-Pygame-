from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
     def __init__(self,set,screen,ship,bullets):
         super(Bullet,self).__init__()
         self.screen=screen
         self.set=set
         self.rect=pygame.Rect(0,0,set.bullet_width,set.bullet_height)
         self.rect.centerx=ship.rect.centerx
         self.rect.top=ship.rect.top
         self.color=set.bullet_color
         self.speed=set.bullet_speed
         self.bs=bullets

     def update(self):
            print(str(self.rect.top))
            """优化子弹超出屏幕后不继续添加"""
            if self.rect.top>0-self.set.bullet_height:
               self.rect.top-=self.speed



     def drawbullet(self):
         """优化子弹超出屏幕后不在添加"""
         if self.rect.top > 0 - self.set.bullet_height:
             pygame.draw.rect(self.screen,self.color,self.rect)
         else:
             """子弹超出屏幕后移除子弹"""
             self.bs.remove(self)












