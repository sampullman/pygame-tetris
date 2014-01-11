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
    new_level_timer = 0
    start_time = 0

    while True:
        gamestep_timer += clock.tick(FPS)
        if world.difficulty == LEVELS and world.started and ((pygame.time.get_ticks()-start_time)//20000 == 1 or world.lines_cleared >= world.curr_level*10):
            world.new_level()

        if gamestep_timer > timestep and world.started:
            gamestep_timer = 0
            world.update()
            timestep = INITIAL_SPEED - (world.lines_cleared * 8)

        # Gather Events
        pygame.event.pump()

        # Handle mouse input
        world.handle_mouse()

        # Handle keyboard input
        keystate = pygame.key.get_pressed()
        if keystate[K_ESCAPE] or pygame.event.peek(QUIT):
            break
        world.handle_keys(keystate)

        world.clear(screen)
        world.draw(screen)

        pygame.display.flip()
        if world.start_of_level and world.started:
            world.start_of_level = False
            pygame.time.wait(1000)
            start_time = pygame.time.get_ticks()

        
    pygame.time.wait(50)

def restart(world, screen):
    world.clear(screen)
    world.new_level()

#if python says run, let's run!
if __name__ == '__main__':
    main()
