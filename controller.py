import pygame

import model


def controller():
    events=pygame.event.get()
    model.button_coins_add.controller(events)
    model.button_upgrade_worker2.controller(events)
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
            model.money_get()