import pygame,image,text
pygame.init()
screen=pygame.display.set_mode([800*1.5,533*1.5])
import model







worker1=image.Image(1/3,"sprites/worker/worker1.png",screen,0,550)
coin=image.Image(1/2,'sprites/controls/coin.png',screen,850,60)
plus=image.Image(1/5,"sprites/controls/plus.png",screen,850,110)


def view():
    screen.fill([0,0,0])
    model.current_city.blit()
    if not model.clear_all:
        worker1.blit()
        coin.blit()
        plus.blit()
        model.coins.blit()
        model.coins_add.blit()
        model.button_coins_add.blit()
        model.lvl_player.blit()
        model.cost_for_upgrade_player.blit()
        model.coins_per_click_add.blit()
        model.coins_at_second.blit()
        model.worker2.blit()
        model.worker3.blit()
        model.worker4.blit()
        model.worker5.blit()
    pygame.display.set_caption(str(int(model.clock.get_fps())))
    pygame.display.flip()