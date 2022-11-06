import pygame
import LoadImage as l


pygame.init()


WHITE=[255,255,255]
SCREEN_WIDTH=(400)
SCREEN_HEIGHT=(680)

tilesetList=['Tech_dungeon/Players/players blue x1.png']
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

done=False
clock=pygame.time.Clock()
walkcnt=0

p_run_ani=[l.LoadSprite(tilesetList[0],0,96,32,32),
    l.LoadSprite(tilesetList[0],32,96,32,32),
    l.LoadSprite(tilesetList[0],64,96,32,32),
    l.LoadSprite(tilesetList[0],96,96,32,32),]

#Run=l.LoadTileset(tilesetList[0],Run,0,96,32,32,4)


def runGame():
    global done,p_run_ani,walkcnt
    p_posX=20
    p_posY=24
    run=False
    moveSpeed=20

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    run=True
                    if run: p_posY-=20
                if event.key==pygame.K_s:
                    run=True
                    if run: p_posY+=20
                if event.key==pygame.K_a:
                    run=True
                    if run: p_posX-=20
                if event.key==pygame.K_d:
                    run=True
                    if run: p_posX+=20
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    run=False
                if event.key==pygame.K_s:
                    run=False
                if event.key==pygame.K_a:
                    run=False
                if event.key==pygame.K_d:
                    run=False
               
        if walkcnt>3: walkcnt=0
        screen.blit(p_run_ani[walkcnt],(p_posX,p_posY))
        

        pygame.display.update()

runGame()
pygame.quit()
