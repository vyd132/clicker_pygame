import pygame,text,button
pygame.init()

clock=pygame.time.Clock()

coins_add=text.Text([0,255,0],60,pygame.display.get_surface(),1000,100,'+',2,'')
lvl_player=text.Text([255,255,255],40,pygame.display.get_surface(),20,500,'Уровень ',0,'')
coins=text.Text('#EBB401',60,pygame.display.get_surface(),1000,50,'$',0,'')
cost_for_upgrade_player=text.Text([0,255,0],40,pygame.display.get_surface(),450,110,'Цена ',10,' за улучшение')
coins_per_click_add=text.Text([0,255,0],40,pygame.display.get_surface(),450,160,'+ ',2,' за улучшение')


def coins_add_click():
    global coins_per_click_add
    if buy(1.05,cost_for_upgrade_player)==False:
        print(coins_add._number)
        return
    coins_add.number_for_text+=coins_per_click_add.number_for_text
    lvl_player.number_for_text+=1
    coins_per_click_add.number_for_text+=2

def money_get():
    coins.number_for_text+=coins_add.number_for_text

def buy(cost_increase,upgrade_cost):
    if coins.number_for_text>=upgrade_cost.number_for_text:
        coins.number_for_text-=upgrade_cost.number_for_text
        upgrade_cost.number_for_text*=cost_increase
        print('work')
        return True
    else:
        return False




button_coins_add=button.Button(1/4,'sprites/controls/up_green.png',pygame.display.get_surface(),890,110,coins_add_click)
# city=