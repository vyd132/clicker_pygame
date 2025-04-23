import pygame

class Text():
    def __init__(self,color,size,screen,x,y,text_first,number,text_last):
        self.font = pygame.font.SysFont('Arial', size)
        self.color=color
        self.screen=screen
        self.x=x
        self.y=y
        self.text_first=text_first
        self.text_last=text_last
        self._number=number
        self.render()


    def blit(self):
        self.screen.blit(self.text_surface,[self.x,self.y])

    def render(self):
        self.text_surface = self.font.render(self.text_first + str(int(self._number)) + self.text_last, True, self.color)

    @property
    def number_for_text(self):
        return self._number

    @number_for_text.setter
    def number_for_text(self,new):
        self._number=new
        self.render()

