from  pygame.sprite import Sprite
import pygame
class Alien(Sprite):

    def __init__(self,set,screen,aliens):
        super(Alien,self).__init__()
        self.image = pygame.image.load('D:\AlineGame\image\wxr.jpg')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect=self.image.get_rect()
        print("kuan:"+str(self.rect.width)+"gao:"+str(self.rect.height))
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.screen=screen
        self.aliens=aliens
        self.set=set
        self.moveRight=True



    def judgeNumeInScreenLine(self):
        w,h=self.screen.get_size()
        """去除左边右边的距离剩下的能放外星人的总宽度"""
        normaltotalwidth=w-self.rect.width*2
        return  normaltotalwidth/self.rect.width/2


    def blitme(self):
        self.screen.blit(self.image,self.rec)


    def update(self):
        self.update_bottom()
        if(self.rect.right<self.screen.get_rect().right and self.moveRight):
                self.rect.x+=self.set.alines_speed

        elif self.rect.right>=self.screen.get_rect().right:
            self.moveRight=False
            self.rect.x-=self.set.alines_speed
            self.rect.y+=self.set.alines_speedh
        elif self.rect.left<=self.screen.get_rect().left:
            self.moveRight=True
            self.rect.x+=self.set.alines_speed
            self.rect.y+=self.set.alines_speedh
        else:
            self.rect.x-= self.set.alines_speed



    """检测是不是到了底部"""
    def update_bottom(self):
        if self.rect.bottom>=self.screen.get_rect().bottom:
            """外星人碰撞到了底部了"""
            return True
        else:
            return None





