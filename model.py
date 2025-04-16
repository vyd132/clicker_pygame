import pygame,text,button
pygame.init()

clock=pygame.time.Clock()

coins_add=text.Text([0,255,0],60,pygame.display.get_surface(),1000,100,'+',2,'')
lvl_player=text.Text([255,255,255],40,pygame.display.get_surface(),20,500,'Уровень ',0,'')
coins=text.Text('#EBB401',60,pygame.display.get_surface(),1000,50,'$',0,'')




def coins_add_click():
    coins_add.number_for_text+=2
    lvl_player.number_for_text+=1

def money_get():
    coins.number_for_text+=coins_add.number

button_coins_add=button.Button(1/4,'sprites/controls/up_green.png',pygame.display.get_surface(),890,110,coins_add_click)
# city=