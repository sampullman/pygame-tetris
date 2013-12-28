import random, os.path, sys
import pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]  # Program's diretory

FPS = 25
SCREENRECT = Rect(0, 0, 640, 600)

def main():
    # Initialize SDL components
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size, 0)
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

#if python says run, let's run!
if __name__ == '__main__':
    main()
