import random, os.path, sys
import pygame
from pygame.locals import *
from world import *
from constants import *

SCREENRECT = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def main():
    
    # Initialize SDL components
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size, 0)
    screen.fill(BG_COLOR, SCREENRECT)
    load_images()
    clock = pygame.time.Clock()
    timestep = INITIAL_SPEED
    gamestep_timer = 0

    world = World()

    while True:
        gamestep_timer += clock.tick(FPS)
        if gamestep_timer > timestep:
            gamestep_timer = 0
            world.update()
            timestep = INITIAL_SPEED - (world.lines_cleared * 10)
        if world.game_over:
            break

        # Gather Events
        pygame.event.pump()
        keystate = pygame.key.get_pressed()
        if keystate[K_ESCAPE] or pygame.event.peek(QUIT):
            break

        world.handle_input(keystate)

        world.clear(screen)
        world.draw(screen)

        pygame.display.flip()
        
    pygame.time.wait(50)

#if python says run, let's run!
if __name__ == '__main__':
    main()
