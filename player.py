import pygame

class Player:

    def __init__(self,file,hp,ad,df,v):
        self.hp=hp
        self.ad=ad
        self.df=df
        self.v=v
        self.sprite=[]

        #movement
        self.run=False
        self.AniDir='right'
        self.dir=''
        self.x=0
        self.y=0
        

        #init sprite
        self.image=pygame.image.load(file).convert()
        self.sprite=[self.image.subsurface(0,96,32,32),
                    self.image.subsurface(32,96,32,32),
                    self.image.subsurface(64,96,32,32),
                    self.image.subsurface(96,96,32,32)]

    def update(self):
        pass



    
    

    
  
            

    
