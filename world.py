import os
import pygame
from pygame import draw
from pygame.locals import *

from constants import *
from block import *
import block

class World:
    def __init__(self):
        self.board = Board(Cell(BOARD_OFFSET_X, BOARD_OFFSET_Y), BOARD_WIDTH, BOARD_HEIGHT)
        self.player_block = generate(int(BOARD_WIDTH/2), 0)
        self.next_block = generate(1, 2)
        self.preview_rect = (PREVIEW_OFFSET_X*CELL_WIDTH, PREVIEW_OFFSET_Y*CELL_WIDTH,
                             CELL_WIDTH*PREVIEW_WIDTH, CELL_HEIGHT*PREVIEW_HEIGHT)
        self.keys = { K_LEFT: False, K_RIGHT: False, K_DOWN: False, K_UP: False }
        self.game_over = False
        self.large_font = pygame.font.Font(None, 40)
        self.medium_font = pygame.font.Font(None, 32)
        self.next_text = self.large_font.render("Next", 1, FONT_COLOR)
        self.next_text_pos = self.next_text.get_rect(center=((PREVIEW_OFFSET_X+PREVIEW_WIDTH/2)*CELL_WIDTH,
                                                             PREVIEW_OFFSET_Y*CELL_WIDTH-self.next_text.get_height()/2))
        self.lines_text = self.large_font.render("Lines: ", 1, FONT_COLOR)
        self.lines_text_pos = self.lines_text.get_rect(topleft=((BOARD_WIDTH+BOARD_OFFSET_X+1)*CELL_WIDTH, SCREEN_HEIGHT/2))
        self.cleared_text = self.large_font.render("0", 1, FONT_COLOR)
        self.cleared_text_pos = self.cleared_text.get_rect(topleft=(self.lines_text_pos.right+10, SCREEN_HEIGHT/2))
        self.lines_cleared = 0

    def clear(self, screen):
        screen.fill(BG_COLOR, self.preview_rect)
        screen.fill(BG_COLOR, self.cleared_text_pos)
        self.board.clear(screen)

    def draw(self, screen):
        draw.rect(screen, OUTLINE_COLOR, self.preview_rect, 2)
        self.player_block.draw(screen, BOARD_OFFSET_X, BOARD_OFFSET_Y)
        self.next_block.draw(screen, PREVIEW_OFFSET_X, PREVIEW_OFFSET_Y)
        self.board.draw(screen)
        screen.blit(self.next_text, self.next_text_pos)
        screen.blit(self.lines_text, self.lines_text_pos)
        screen.blit(self.cleared_text, self.cleared_text_pos)

    def update(self):
        self.player_block.update()
        # check to see if the player block now overlaps any other blocks
        if self.board.overlaps(self.player_block):
            self.player_block.move(UP)
            lines_cleared = self.board.add_blocks(self.player_block)
            if lines_cleared > 0:
                self.lines_cleared += lines_cleared
                self.cleared_text = self.large_font.render(str(self.lines_cleared), 1, FONT_COLOR)
            self.player_block = self.next_block
            self.player_block.topLeft = (4, 0)
            if self.board.overlaps(self.player_block):
                self.game_over = True
            self.next_block = generate(1, 2)
        self.board.update()

    def handle_input(self, keystate):
        if keystate[K_RIGHT] and not self.keys[K_RIGHT]:
            self.player_block.move(RIGHT)
            if self.board.overlaps(self.player_block):
                self.player_block.move(LEFT)
        elif keystate[K_LEFT] and not self.keys[K_LEFT]:
            self.player_block.move(LEFT)
            if self.board.overlaps(self.player_block):
                self.player_block.move(RIGHT)
        elif keystate[K_UP] and not self.keys[K_UP]:
            self.player_block.rotate(ROT_RIGHT)
            if self.board.overlaps(self.player_block):
                self.player_block.rotate(ROT_LEFT)
        elif keystate[K_SPACE] and not self.keys[K_SPACE]:
            self.finish_player_block();
        self.keys[K_RIGHT] = keystate[K_RIGHT]
        self.keys[K_LEFT] = keystate[K_LEFT]
        self.keys[K_UP] = keystate[K_UP]
        self.keys[K_SPACE] = keystate[K_SPACE]

    def finish_player_block(self):
        while not self.board.overlaps(self.player_block):
            self.player_block.move(DOWN)
        self.player_block.move(UP)

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:

    def __init__(self, topLeft, width, height):
        self.origin = Cell(topLeft.x*CELL_WIDTH, topLeft.y*CELL_HEIGHT)
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.outline_rect = (self.origin.x-2, self.origin.y-2, width * CELL_WIDTH+3, height * CELL_HEIGHT+3)

    def clear(self, screen):
        screen.fill(BG_COLOR, self.outline_rect)

    def draw(self, screen):
        draw.rect(screen, OUTLINE_COLOR, self.outline_rect, 2)
        pos = [0, self.origin.y]
        for row in self.board:
            pos[0] = self.origin.x
            for cell in row:
                if cell != 0:
                    screen.blit(block.blocks[cell], pos)
                pos[0] += CELL_WIDTH
            pos[1] += CELL_HEIGHT

    def overlaps(self, block):
        if block.lowest() >= BOARD_HEIGHT:
            return True
        for i in range(len(block.cells)):
            for j in range(len(block.cells[0])):
                if block.cells[i][j] == 1:
                    xpos = block.topLeft[0]+j
                    ypos = block.topLeft[1]+i
                    if self.board[ypos][xpos] != 0:
                        return True
        return False

    # Probably don't need this for anything :/ Returns array of the top layer of blocks
    def top_layer(self):
        layer = [BOARD_HEIGHT for x in range(BOARD_WIDTH)]
        for i in range(BOARD_HEIGHT-1, -1, -1):
            done = 0
            for j in range(BOARD_WIDTH):
                if self.board[i][j] == 0:
                    done += 1
                else:
                    layer[j] = i
        return layer

    def add_blocks(self, block):
        lines_to_check = set()
        lines_cleared = 0
        for i in range(len(block.cells)):
            for j in range(len(block.cells[0])):
                if block.cells[i][j] == 1:
                    ypos = block.topLeft[1]+i
                    self.board[ypos][block.topLeft[0]+j] = block.color
                    lines_to_check.add(ypos)
        for line in lines_to_check:
            clear = True
            for block in self.board[line]:
                if block == 0:
                    clear = False
            if clear:
                self.board.pop(line)
                self.board.insert(0, [0 for x in range(BOARD_WIDTH)])
                lines_cleared += 1
        return lines_cleared

    def update(self):
        pass
