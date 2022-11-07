import pygame
from __init__ import Game


if __name__=='__main__':
    game=Game()


    while True:
        game.handle_event()
        game.update()
        game.draw()


