import os
import pygame
from pygame import draw

from constants import *

def load_image(file, transparent=0):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' %
                         (file, pygame.get_error()))
    if transparent:
        corner = surface.get_at((0, 0))
        surface.set_colorkey(corner, RLEACCEL)
    return surface.convert()

blocks = []

def load_images():
    global blocks
    blocks = ["", load_image('red_block.png'), load_image('yellow_block.png'), load_image('purple_block.png'),
              load_image('green_block.png'),load_image('blue_block.png'), load_image('orange_block.png'), load_image('cyan_block.png')]
    for i in range(1, len(blocks)):
        blocks[i] = pygame.transform.smoothscale(blocks[i], (CELL_WIDTH, CELL_HEIGHT))

class World:
    def __init__(self):
        self.board = Board(Cell(CELL_WIDTH*2, CELL_HEIGHT*2), BOARD_WIDTH, BOARD_HEIGHT)

    def clear(self, screen):
        self.board.clear(screen)

    def draw(self, screen):
        self.board.draw(screen)

    def update(self):
        self.board.update()

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:

    def __init__(self, topLeft, width, height):
        self.origin = topLeft
        self.width = width
        self.height = height
        self.board = [[x % len(blocks) for x in range(width)] for y in range(height)]
        self.outline_color = (180, 180, 190)
        self.outline_rect = (topLeft.x-2, topLeft.y-2, width * CELL_WIDTH+3, height * CELL_HEIGHT+3)

    def clear(self, screen):
        screen.fill(BG_COLOR, self.outline_rect)

    def draw(self, screen):
        draw.rect(screen, self.outline_color, self.outline_rect, 2)
        pos = [0, self.origin.y]
        for row in self.board:
            pos[0] = self.origin.x
            for cell in row:
                if cell != 0:
                    screen.blit(blocks[cell], pos)
                pos[0] += CELL_WIDTH
            pos[1] += CELL_HEIGHT

    def update(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = (self.board[i][j] + 1) % len(blocks)
