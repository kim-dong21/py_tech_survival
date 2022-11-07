import pygame


class tilesheet:
    def __init__(self,file,w,h,rows,cols):
        image=pygame.image.load(file).convert()
        self.tile_table=[]

        for tile_x in range(0,cols):
            line=[]
            self.tile_table.append(line)
            for tile_y in range(0,rows):
                rect=(tile_x*w,tile_y*h,w,h)
                line.append(image.subsurface(rect))



    def draw(self,screen):
        for x,row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile,(x*72,y*72))

class player_sprite:
    def __init__(self,):
        
    

