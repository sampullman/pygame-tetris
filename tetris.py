import random, os.path, sys
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]  # Program's diretory

def main():
    # Initialize SDL components
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size, 0)
    clock = pygame.time.Clock()

#if python says run, let's run!
if __name__ == '__main__':
    main()
