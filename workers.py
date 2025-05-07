import pygame,image

class Workers():
    def __init__(self,img_inv,img_normal,x,y,cost):
        self.img_inv=image.Image(1/3,img_inv,pygame.display.get_surface(),x,y)
        self.img_normal = image.Image(1/3,img_normal,pygame.display.get_surface(),x,y)
        self.x=x
        self.y=y
        self.cost=cost


