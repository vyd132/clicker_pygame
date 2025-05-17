import pygame,image,text,button

class Workers():
    def __init__(self, img_inv, img_normal, x, y, cost,buy,visible,increase,income,next_worker=None):
        self.img_inv = image.Image(1 / 3, img_inv, pygame.display.get_surface(), x, y)
        self.img_normal = image.Image(1 / 3, img_normal, pygame.display.get_surface(), x, y)
        self.lvl_worker = text.Text([255, 255, 255], 40, pygame.display.get_surface(), x, y - 60, 'Уровень ', 0, '',
                                    '#135B0F')
        self.button_upgrade_worker = button.Button(1 / 6, 'sprites/controls/up_yellow.png',
                                                pygame.display.get_surface(), x+self.img_normal.image.get_width()/1.6,y+self.img_normal.image.get_height()/2+7, self.workers_upgrade)

        self.x = x
        self.y = y
        self.cost_for_upgrade = text.Text('#EBB401', 40, pygame.display.get_surface(),x+self.img_normal.image.get_width()/1.3,y+self.img_normal.image.get_height()/2, '', cost, '', '#543F01')
        self.buy=buy
        self.visible=visible
        self.next_worker=next_worker
        self.income=income
        self.increase=increase
        self.income_text = text.Text([255, 0, 0], 40, pygame.display.get_surface(),
                                     x + self.img_normal.image.get_width() / 1.3,
                                     y + self.img_normal.image.get_height() / 2+50, '+', self.increase,'','#750E13')

    def workers_upgrade(self):
        if self.buy(1.05, self.cost_for_upgrade) == False:
            return
        # coins_add.number_for_text += coins_per_click_add.number_for_text
        self.lvl_worker.number_for_text += 1
        self.income.number_for_text += self.income_text.number_for_text
        self.income_text.number_for_text += self.increase
        if self.lvl_worker.number_for_text >=10 and  self.next_worker!=None:
            self.next_worker.visible=True


    def blit(self):
        if not self.visible:
            return
        if self.lvl_worker.number_for_text==0:
            self.img_inv.blit()
        else:
            self.img_normal.blit()
        self.lvl_worker.blit()
        self.button_upgrade_worker.blit()
        self.cost_for_upgrade.blit()
        self.income_text.blit()

    def controller(self,events):
        if self.visible:
            self.button_upgrade_worker.controller(events)









