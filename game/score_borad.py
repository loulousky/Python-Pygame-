import pygame
class Score_Borad():
    def __init__(self,screen,setting,gamestate):
        self.screen=screen
        self.setting=setting
        self.gamestate=gamestate
        self.font=pygame.font.SysFont(None,48)
        self.textcolor=(0,0,0)

    def draw_score(self):

        """圆整"""
        round_score=round(self.gamestate.score)
        score_str="{:,}".format(round_score)
        self.image=self.font.render(score_str,True,self.textcolor,(255,255,255))
        self.rect=self.image.get_rect()
        self.rect.top=20
        self.rect.right=self.screen.get_rect().right-20
        self.screen.blit(self.image,self.rect)
        self.draw_lift()
        self.draw_highscore()

    def draw_lift(self):
        for x in range(self.setting.ship_limit):
            image = pygame.image.load('D:\AlineGame\image\ship.bmp')
            image = pygame.transform.scale(image, (30, 40))
            imagerect=image.get_rect()
            imagerect.left=self.screen.get_rect().left+20+30*x
            imagerect.top = 20
            self.screen.blit(image,imagerect)


    def draw_highscore(self):
        if(self.gamestate.score>self.gamestate.high_score):
            self.gamestate.high_score=self.gamestate.score
            with open("D:/AlineGame/text/aaa.text","w") as f:
                f.write(str(self.gamestate.high_score))
        else:
            with open("D:/AlineGame/text/aaa.text") as f:
                  if len(f.read())>0:
                      f.seek(0)
                      self.gamestate.high_score=int(f.readline())
        roundsroce=round(self.gamestate.high_score)
        str_highscore="{:,}".format(roundsroce)
        hight_score_image=self.font.render(str_highscore,True,self.textcolor,(255,255,255))
        higt_score_rec=hight_score_image.get_rect()
        higt_score_rec.centerx=self.screen.get_rect().centerx
        higt_score_rec.top=20
        self.screen.blit(hight_score_image,higt_score_rec)


