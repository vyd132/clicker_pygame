import pygame,text
pygame.init()

clock=pygame.time.Clock()
coins_add=2

coins=text.Text('#EBB401',60,pygame.display.get_surface(),1000,50,'$',0,'')


def money_get():
    global coins
    coins.number_for_text+=coins_add

# city=