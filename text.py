import pygame,text_for_number

class Text():
    def __init__(self,color,size,screen,x,y,text_first,number,text_last,background_color):
        self.font = pygame.font.SysFont('Arial', size)
        self.color=color
        self.screen=screen
        self.x=x
        self.y=y
        self.text_first=text_first
        self.text_last=text_last
        self._number=number
        self._text_number = str(number)
        self.background_color=background_color
        self.render()



    def blit(self):
        self.screen.blit(self.text_surface,[self.x,self.y])

    def render(self):
        self._text_number=text_for_number.text(self._number,['K','M','B','T'])
        self.text_surface = self.font.render(self.text_first + self._text_number + self.text_last, True, self.color,self.background_color)

    @property
    def number_for_text(self):
        return self._number

    @number_for_text.setter
    def number_for_text(self,new):
        self._number=new
        self.render()

    # def text(self):
    #         print(self._number)
    #         self._text_number=''
    #         if self._number//1000000!=0:
    #             self._text_number=str(int(self._number)//1000000)+'M '
    #         remainder_from_division=int(self._number)%1000000
    #         if remainder_from_division//1000!=0:
    #             self._text_number = self._text_number + str(remainder_from_division // 1000) + 'K '
    #         if remainder_from_division%1000!=0:
    #             self._text_number=self._text_number+str(remainder_from_division%1000)
    #         if self._number==0:
    #             self._text_number = str(0)


