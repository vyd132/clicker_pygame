import pygame,workers,image

class Business(workers.Workers):
    def __init__(self,img_inv, img_normal1,img_normal2,img_normal3, x, y,size, cost,buy,visible,increase,income,next_worker=None,on_lvl_10=None,background_level=10):
        workers.Workers.__init__(self,img_inv, img_normal1, x, y,size, cost,buy,visible,increase,income,next_worker,on_lvl_10,background_level)
        self.img_normal2=image.Image(size, img_normal2, pygame.display.get_surface(), x, y)
        self.img_normal3 = image.Image(size, img_normal3, pygame.display.get_surface(), x, y)
    def draw_body(self):
        if self.lvl_worker.number_for_text >= 20:
            self.img_normal3.blit()
        elif self.lvl_worker.number_for_text>=10:
            self.img_normal2.blit()
        elif self.lvl_worker.number_for_text>=1:
            self.img_normal.blit()
        elif self.lvl_worker.number_for_text == 0:
            self.img_inv.blit()


