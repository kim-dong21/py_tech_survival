import pygame
import sys
import tilesheet
import player as p
class Game:
    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((1280,640))
        self.clock=pygame.time.Clock()

        self.bg_color=pygame.Color((255,255,255))

        self.tiles=tilesheet.tilesheet('Tech_dungeon/Players/players blue x1.png',32,32,13,8)
        
        self.p1=p.Player(self.tiles.tile_table,24,4)
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
        