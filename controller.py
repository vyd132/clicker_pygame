import pygame

def controller():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()