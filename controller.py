import pygame

import model

income=pygame.event.custom_type()
pygame.time.set_timer(income,1000)


def controller():
    events=pygame.event.get()
    model.button_coins_add.controller(events)
    for worker in model.workers_list:
        worker.controller(events)
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
            model.money_get()
        if event.type==income:
            model.coins.number_for_text+=model.coins_at_second.number_for_text