import pygame,model
pygame.init()
screen=pygame.display.set_mode([800*1.5,533*1.5])
city=pygame.image.load("sprites/place/place1.jpg")
city=pygame.transform.scale(city,[800*1.5,533*1.5])
worker1=pygame.image.load("sprites/worker/worker1.png")
worker1=pygame.transform.scale(worker1,[614/3,713/3])
font=pygame.font.SysFont('Arial',60)
text=font.render(str(model.coins),True,'#EBB401')
coin=pygame.image.load('sprites/controls/coin.png')
coin=pygame.transform.scale(coin,[87/2,87/2])



def view():
    screen.fill([0,0,0])
    screen.blit(city,[0,0])
    screen.blit(worker1,[0,550])
    screen.blit(text,[1000,50])
    screen.blit(coin,[950,60])
    pygame.display.set_caption(str(int(model.clock.get_fps())))
    pygame.display.flip()