import pygame

class Player:

    def __init__(self,sprite,idx,f):
        self.ani=[]
        for i in range(f):
            self.ani=sprite[idx]
            idx+=1

    
    def draw(self,screen,x,y):
        screen.blit(self.ani,x,y)
            

    
