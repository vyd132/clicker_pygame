import pygame,text,button,workers
pygame.init()
workers_list=[]
clock=pygame.time.Clock()

coins_add=text.Text([0,255,0],40,pygame.display.get_surface(),900,110,'',2,'','#135B0F')
lvl_player=text.Text([255,255,255],40,pygame.display.get_surface(),20,500,'Уровень ',0,'','#135B0F')
coins=text.Text('#EBB401',40,pygame.display.get_surface(),900,60,'$',1000000000,'','#543F01')
cost_for_upgrade_player=text.Text([0,255,0],40,pygame.display.get_surface(),450,150,'Цена ',10,' за улучшение','#135B0F')
coins_per_click_add=text.Text([0,255,0],40,pygame.display.get_surface(),450,200,'+ ',2,' за улучшение','#135B0F')
coins_at_second=text.Text([255, 0, 0], 40, pygame.display.get_surface(),900,160
                                     , '', 0,'','#750E13')



def coins_add_click():
    if buy(1.05,cost_for_upgrade_player)==False:
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
        return True
    else:
        return False

worker3=workers.Workers("sprites/worker/worker3_inv.png","sprites/worker/worker3.png",600,350,1000000,buy,False,5,coins_at_second)
workers_list.append(worker3)

worker2=workers.Workers("sprites/worker/worker2_inv.png","sprites/worker/worker2.png",300,350,10000,buy,True,1,coins_at_second,worker3)
workers_list.append(worker2)




button_coins_add=button.Button(1/4,'sprites/controls/up_green.png',pygame.display.get_surface(),800,110,coins_add_click)
# city=