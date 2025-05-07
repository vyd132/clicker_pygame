import pygame,text,button
pygame.init()

clock=pygame.time.Clock()

coins_add=text.Text([0,255,0],40,pygame.display.get_surface(),900,110,'',2,'','#135B0F')
lvl_player=text.Text([255,255,255],40,pygame.display.get_surface(),20,500,'Уровень ',0,'','#135B0F')
coins=text.Text('#EBB401',40,pygame.display.get_surface(),900,60,'$',1000000000,'','#543F01')
cost_for_upgrade_player=text.Text([0,255,0],40,pygame.display.get_surface(),450,150,'Цена ',10,' за улучшение','#135B0F')
coins_per_click_add=text.Text([0,255,0],40,pygame.display.get_surface(),450,200,'+ ',2,' за улучшение','#135B0F')
lvl_worker2=text.Text([255,255,255],40,pygame.display.get_surface(),300,300,'Уровень ',0,'','#135B0F')
cost_for_upgrade_worker2=text.Text('#EBB401',40,pygame.display.get_surface(),530,395,'',10000,'','#543F01')


def coins_add_click():
    if buy(1.05,cost_for_upgrade_player)==False:
        return
    coins_add.number_for_text+=coins_per_click_add.number_for_text
    lvl_player.number_for_text+=1
    coins_per_click_add.number_for_text+=2

def workers_upgrade():
    if buy(1.05, cost_for_upgrade_worker2) == False:
        return
    # coins_add.number_for_text += coins_per_click_add.number_for_text
    lvl_worker2.number_for_text += 1


def money_get():
    coins.number_for_text+=coins_add.number_for_text

def buy(cost_increase,upgrade_cost):
    if coins.number_for_text>=upgrade_cost.number_for_text:
        coins.number_for_text-=upgrade_cost.number_for_text
        upgrade_cost.number_for_text*=cost_increase
        return True
    else:
        return False



button_coins_add=button.Button(1/4,'sprites/controls/up_green.png',pygame.display.get_surface(),800,110,coins_add_click)
button_upgrade_worker2=button.Button(1/6,'sprites/controls/up_yellow.png',pygame.display.get_surface(),500,400,workers_upgrade)
# city=