import pygame
import sys
import tilesheet
import player as p

tileset_list=[
    'Tech_dungeon/Players/players blue x1.png',
    'Tech_dungeon/Players/players red x1.png',
    'Tech_dungeon/Players/players green x1.png',
    'Tech_dungeon/Players/players grey x1.png']


class Game:
    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((1280,640))
        self.clock=pygame.time.Clock()
        self.bg_color=pygame.Color((255,255,255))

        
        #init player
        self.p1=p.Player(tileset_list[0],30,5,5,5)
        
                    
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type==pygame.K_DOWN:
            #     if event.key==pygame.K_w:
            #         self.p1.run=True
            #         self.p1.v=10
            #     if event.key==pygame.K_s:
            #         self.p1.run=True
            #         self.p1.v=10
            #     if event.key==pygame.K_a:
            #         self.p1.run=True
            #         self.p1.AniDir='left'
            #         self.p1.v=10
            #     if event.key==pygame.K_d:
            #         self.p1.run=True
            #         self.p1.AniDir='right'
            #         self.p1.v=10
            key=pygame.key.get_pressed()
            if key[pygame.K_a]:
                self.p1.x-=10
            if key[pygame.K_d]:
                self.p1.x+=10
            if key[pygame.K_w]:
                self.p1.y-=10
            if key[pygame.K_s]:
                self.p1.y+=10


            if event.type==pygame.K_UP:
                if event.key==pygame.K_w and event.key==pygame.K_s and event.key==pygame.K_a and event.key==pygame.K_d:
                    self.p1.run=False
                    self.p1.v=0
                
        
        

    def update(self):
        pass

    def draw(self):
        self.clock.tick(60)
        self.screen.fill(self.bg_color)
        self.screen.blit(self.p1.sprite[0],(self.p1.x,self.p1.y))
        pygame.display.flip()
        