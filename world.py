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
        self.next_block = generate(int(PREVIEW_WIDTH/2), 0)
        self.preview_rect = (PREVIEW_OFFSET_X*CELL_WIDTH, PREVIEW_OFFSET_X*CELL_WIDTH,
                             CELL_WIDTH*PREVIEW_WIDTH, CELL_HEIGHT*PREVIEW_HEIGHT)
        self.keys = { K_LEFT: False, K_RIGHT: False, K_DOWN: False, K_UP: False }

    def clear(self, screen):
        screen.fill(BG_COLOR, self.preview_rect)
        self.board.clear(screen)

    def draw(self, screen):
        draw.rect(screen, OUTLINE_COLOR, self.preview_rect, 2)
        self.player_block.draw(screen, BOARD_OFFSET_X, BOARD_OFFSET_Y)
        self.board.draw(screen)

    def update(self):
        self.player_block.update()
        # check to see if the player block now overlaps any other blocks
        if self.board.overlaps(self.player_block):
            self.player_block.move(UP)
            self.board.add_blocks(self.player_block)
            self.player_block = self.next_block
            self.next_block = generate(int(BOARD_WIDTH/2), 0)
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
        self.keys[K_RIGHT] = keystate[K_RIGHT]
        self.keys[K_LEFT] = keystate[K_LEFT]
        self.keys[K_UP] = keystate[K_UP]

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
        print block.lowest(), BOARD_HEIGHT
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
        for i in range(len(block.cells)):
            for j in range(len(block.cells[0])):
                if block.cells[i][j] == 1:
                    print block.topLeft[1]+i, block.topLeft[0]+j
                    self.board[block.topLeft[1]+i][block.topLeft[0]+j] = block.color

    def update(self):
        pass
