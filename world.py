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
        self.keys = { K_LEFT: False, K_RIGHT: False, K_DOWN: False }

    def clear(self, screen):
        screen.fill(BG_COLOR, self.preview_rect)
        self.board.clear(screen)

    def draw(self, screen):
        draw.rect(screen, OUTLINE_COLOR, self.preview_rect, 2)
        self.player_block.draw(screen)
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
        elif keystate[K_LEFT] and not self.keys[K_LEFT]:
            self.player_block.move(LEFT)
        self.keys[K_RIGHT] = keystate[K_RIGHT]
        self.keys[K_LEFT] = keystate[K_LEFT]

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
        top_layer = self.top_layer()
        return False

    def top_layer(self):
        for i in range(BOARD_HEIGHT-1, -1, -1):
            for j in range(BOARD_WIDTH):
                pass

    def add_blocks(self, block):
        for i in range(len(block.cells)):
            for j in range(len(block.cells[0])):
                if block.cells[i][j] == 1:
                    self.board[block.topLeft[0]+i][block.topLeft[1]+j] = block.color

    def update(self):
        pass
