#coding:utf-8
"""按钮"""
import pygame

class Button():
    def __init__(self,setting,screen,msg):
        self.width=200
        self.height=50
        self.setting=setting
        self.screen=screen
        self.msg=msg
        self.buttoncolor=(0,255,0)
        self.textcolcr=(255,255,255)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen.get_rect().center
        self.font=pygame.font.SysFont("SimHei",48)

        self.showmsg()

    """文字显示到屏幕上"""
    def showmsg(self):
        self.textimage=self.font.render(self.msg,True,self.textcolcr,self.buttoncolor)
        self.textrect=self.textimage.get_rect()
        self.textrect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.buttoncolor,self.rect)
        self.screen.blit(self.textimage,self.textrect)






