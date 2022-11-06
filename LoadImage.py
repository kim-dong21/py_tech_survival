from json import load
import pygame


def LoadTileset(file,AniList,x,y,w,h,f):
    loadedImg=LoadImage(file)
    AniList=[]
    for i in range(f):
        AniList.append(SplitImg(loadedImg,x,y,w,h))
        
    return AniList

def LoadSprite(file,x,y,w,h):
    LoadedImg=LoadImage(file)
    return SplitImg(LoadedImg,x,y,w,h)

def LoadImage(file):
    loadedImg=pygame.image.load(file)
    return loadedImg


def SplitImg(img,x,y,w,h):
    splitImg=img.subsurface([x,y,w,h])

    return splitImg

    