import pygame
class Ship():
    def __init__(self,screen,setting):
        self.screen=screen
        self.set=setting
        self.image=pygame.image.load('D:\AlineGame\image\ship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect=self.image.get_rect()
        self.screenrec=screen.get_rect()
        self.rect.centerx=self.screenrec.centerx

        self.rect.bottom=self.screenrec.bottom
        self.move=False
        self.right=True



    def updata(self):
        if self.move:
            if self.right:
                if self.rect.right<self.screenrec.right:
                    self.rect.centerx+=self.set.speed
            else:
                if self.rect.left>self.screenrec.left:
                    self.rect.centerx+=-self.set.speed



    def blitme(self):
        self.screen.blit(self.image, self.rect)

