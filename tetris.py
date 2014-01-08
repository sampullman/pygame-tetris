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
        (h,i,j) = pygame.mouse.get_pressed()
        if h == True:
            changed_difficulty = False
            mouse_pos = pygame.mouse.get_pos()
            
            if ((mouse_pos[0] > EASY_BUTTON_OFFSET_X*CELL_WIDTH and mouse_pos[0] < (EASY_BUTTON_OFFSET_X+4)*CELL_WIDTH)
                and(mouse_pos[1] > EASY_BUTTON_OFFSET_Y*CELL_HEIGHT and mouse_pos[1] < (EASY_BUTTON_OFFSET_Y+2)*CELL_HEIGHT)):
                changed_difficulty = True
                difficulty = EASY
            elif ((mouse_pos[0] > HARD_BUTTON_OFFSET_X*CELL_WIDTH and mouse_pos[0] < (HARD_BUTTON_OFFSET_X+4)*CELL_WIDTH)
                and(mouse_pos[1] > EASY_BUTTON_OFFSET_Y*CELL_HEIGHT and mouse_pos[1] < (EASY_BUTTON_OFFSET_Y+2)*CELL_HEIGHT)):
                changed_difficulty = True
                difficulty = HARD
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
        if h and changed_difficulty:
            world.handle_difficulty(difficulty)

        world.clear(screen)
        world.draw(screen)

        pygame.display.flip()
        
    pygame.time.wait(50)

#if python says run, let's run!
if __name__ == '__main__':
    main()
