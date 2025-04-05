import pygame

class Image():
    def __init__(self,size,path_to_image,screen,x,y):
        image=pygame.image.load(path_to_image)
        self.image=pygame.transform.scale(image,[image.get_width()*size,image.get_height()*size])
        self.screen=screen
        self.x=x
        self.y=y

    def blit(self):
        self.screen.blit(self.image,[self.x,self.y])

