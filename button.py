import pygame

class Button():
    def __init__(self,size,path_to_image,screen,x,y,command):
        button = pygame.image.load(path_to_image)
        self.button = pygame.transform.scale(button, [button.get_width() * size, button.get_height() * size])
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect([self.x,self.y,self.button.get_width(),self.button.get_height()])
        self.screen=screen
        self.command=command

    def blit(self):
        self.screen.blit(self.button,[self.x,self.y])

    def controller(self,events):
        for event in events:
            if event.type==event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
                if self.cord_check(event.pos):
                    events.remove(event)


    def cord_check(self,pos):
        if self.rect.collidepoint(pos):
            self.command()
            return True
