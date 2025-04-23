import pygame,image,text
pygame.init()
screen=pygame.display.set_mode([800*1.5,533*1.5])
import model






city=image.Image(1.5,"sprites/place/place1.jpg",screen,0,0)
worker1=image.Image(1/3,"sprites/worker/worker1.png",screen,0,550)
coin=image.Image(1/2,'sprites/controls/coin.png',screen,950,60)
plus=image.Image(1/5,"sprites/controls/plus.png",screen,950,110)


def view():
    screen.fill([0,0,0])
    city.blit()
    worker1.blit()
    plus.blit()
    coin.blit()
    model.coins.blit()
    model.coins_add.blit()
    model.button_coins_add.blit()
    model.lvl_player.blit()
    model.cost_for_upgrade_player.blit()
    model.coins_per_click_add.blit()


    pygame.display.set_caption(str(int(model.clock.get_fps())))
    pygame.display.flip()