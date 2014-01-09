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
        if world.started and (pygame.time.get_ticks()-start_time)//20000 == 1 or world.lines_cleared >= world.curr_level*10:
            world.new_level()
            
        (h,i,j) = pygame.mouse.get_pressed()
        if h == True and not world.started:
            changed_difficulty = False
            mouse_pos = pygame.mouse.get_pos()
            
            if ((mouse_pos[0] > ENDLESS_BUTTON_OFFSET_X*CELL_WIDTH and mouse_pos[0] < (ENDLESS_BUTTON_OFFSET_X+4)*CELL_WIDTH)
                and(mouse_pos[1] > ENDLESS_BUTTON_OFFSET_Y*CELL_HEIGHT and mouse_pos[1] < (ENDLESS_BUTTON_OFFSET_Y+2)*CELL_HEIGHT)):
                changed_difficulty = True
                difficulty = ENDLESS
            elif ((mouse_pos[0] > LEVELS_BUTTON_OFFSET_X*CELL_WIDTH and mouse_pos[0] < (LEVELS_BUTTON_OFFSET_X+4)*CELL_WIDTH)
                and(mouse_pos[1] > ENDLESS_BUTTON_OFFSET_Y*CELL_HEIGHT and mouse_pos[1] < (ENDLESS_BUTTON_OFFSET_Y+2)*CELL_HEIGHT)):
                changed_difficulty = True
                difficulty = LEVELS
        if gamestep_timer > timestep and world.started:
            gamestep_timer = 0
            world.update()
            timestep = INITIAL_SPEED - (world.lines_cleared * 10)
        if world.game_over:
            gameover_text = world.large_font.render("GAMEOVER", 1, FONT_COLOR)
            screen.blit(gameover_text, gameover_text.get_rect(topleft=((BOARD_WIDTH/2+BOARD_OFFSET_X-2.5)*CELL_WIDTH, (BOARD_HEIGHT/2+BOARD_OFFSET_Y-2)*CELL_HEIGHT)))
            pygame.display.flip()
            break

        # Gather Events
        pygame.event.pump()
        keystate = pygame.key.get_pressed()
        if keystate[K_ESCAPE] or pygame.event.peek(QUIT):
            break

        world.handle_input(keystate)

        if h and not world.started and changed_difficulty:
            world.handle_difficulty(difficulty)

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
