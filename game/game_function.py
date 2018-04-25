import pygame
import sys
from gameenity import  bullet
from gameenity.alien import Alien
import time
def check_event(ship,bullet,setting,screen,state,button):
    for x in pygame.event.get():
        if x.type==pygame.QUIT:
            sys.exit()
        elif x.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x,mouse_y) and not state.game_active:
               """设置光标不可见"""
               pygame.mouse.set_visible(False)
               state.game_active=True
               state.reset_geme()
        elif x.type==pygame.KEYDOWN:
            check_keydown(x,ship,bullet,setting,screen)
        elif x.type==pygame.KEYUP:
            check_keyup(ship)

def update_screen(screen,ship,setting,bullet,aline,state,button,sb):
    screen.fill(setting.bgcolor)

    """检测飞船和外星人的碰撞"""
    check_failegame(ship,aline,state,screen,setting,bullet)
    if state.game_active:
       ship.updata()
       update_bullets(bullet,aline,state,setting)
       """先画子弹，子弹遮盖住飞机"""
       aline.update()
    ship.blitme()
    aline.draw(screen)
    sb.draw_score()
    if not state.game_active:
        """没开始画BUTTON"""
        button.draw_button()
        pygame.mouse.set_visible(True)
        state.reset_geme()


    pygame.display.flip()


"""飞船和外星人发生碰撞或者外星人到达底部后重置游戏"""
def check_failegame(ship,aline,state,screen,setting,bullet):
    if pygame.sprite.spritecollideany(ship,aline):
        """有命重置游戏继续"""
        if(state.ships_left>0):
            """重置飞船的位置"""
            ship.rect.centerx=ship.screenrec.centerx
            ship.rect.bottom=ship.screenrec.bottom
            bullet.empty()
            aline.empty()
            check_alines(screen,aline,setting,bullet)
            setting.ship_limit-=1
            state.ships_left-=1
            if(state.score>state.high_score):
                state.high_score=state.score
            state.score=0
            time.sleep(1)
        else:
            state.game_active=False
            ship.rect.centerx = ship.screenrec.centerx
            ship.rect.bottom = ship.screenrec.bottom
            bullet.empty()
            aline.empty()
            check_alines(screen, aline, setting, bullet)
            setting.ship_limit = 3
            state.ships_left = 3
            if (state.score > state.high_score):
                state.high_score = state.score
            state.score = 0

            print("游戏应该结束了")
    else:
        """有外星人到达底部"""
        for a in aline:
            if a.update_bottom():
                """重置飞船的位置"""
                if (state.ships_left > 0):
                    """重置飞船的位置"""
                    ship.rect.centerx = ship.screenrec.centerx
                    ship.rect.bottom = ship.screenrec.bottom
                    bullet.empty()
                    aline.empty()
                    check_alines(screen, aline, setting, bullet)
                    setting.ship_limit -= 1
                    state.ships_left -= 1
                    if (state.score > state.high_score):
                        state.high_score = state.score
                    state.score = 0
                    time.sleep(1)
                else:
                    state.game_active = False
                    ship.rect.centerx = ship.screenrec.centerx
                    ship.rect.bottom = ship.screenrec.bottom
                    bullet.empty()
                    aline.empty()
                    check_alines(screen, aline, setting, bullet)
                    setting.ship_limit = 3
                    state.ships_left = 3
                    if (state.score > state.high_score):
                        state.high_score = state.score
                    state.score = 0
                    print("游戏应该结束了")
                break
        pass






"""提取按键按下的事件监听"""
def check_keydown(x,ship,bullets,set,screen):
    if x.key == pygame.K_RIGHT:
        ship.move = True
        ship.right = True
    elif x.key == pygame.K_LEFT:
        ship.move = True
        ship.right = False
    elif x.key==pygame.K_SPACE:
        print("空格")
        create_bullet(set, screen, ship, bullets)
    elif x.key==pygame.K_ESCAPE:
        sys.exit()
    else:
        ship.move = False

"""提取按键抬起的事件监听"""
def check_keyup(ship):
    ship.move = False

def create_bullet(set,screen,ship,bullets):
    new_bullet = bullet.Bullet(set, screen, ship, bullets)
    """子弹个数不能超过10个"""
    if len(bullets) < set.bullet_num:
        bullets.add(new_bullet)
    print(str(len(bullets)))


def update_bullets(bullet,aline,state,setting):
    bullet.update()
    """检查子弹和外星人的碰撞"""
    carsh=pygame.sprite.groupcollide(bullet, aline, True, True)
    for x in carsh.values():
        state.score += len(x) * setting.aline_score
    for x in bullet:
        print("画子弹")
        x.drawbullet()

"""创建一组外星人"""
def create_al(screen,aliens,set):
    """获取宽高"""
    w, h = screen.get_size()
    aline = Alien(set, screen, aliens)
    totle = aline.judgeNumeInScreenLine()
    print("总数"+str(totle))
    for x in range(set.alines_line):
        height = aline.rect.height + aline.rect.height * x
        for number in range(int(totle)):
            al = Alien(set, screen, aliens)
            al.rect.x = al.rect.width + al.rect.width * 2*number
            al.rect.y = height
            aliens.add(al)


"""外星人消灭后重新创建，并把子弹清空"""
def check_alines(screen,aliens,set,bullet):
    if len(aliens)==0:
        create_al(screen,aliens,set)
        bullet.empty()
        set.alines_speed+=1
        set.alines_speedh+=1






