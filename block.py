import pygame
import random

from constants import *

def add(x, y):
    return x + y

blocks = []

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

def load_images():
    global blocks
    blocks = ["", load_image('red_block.png'), load_image('yellow_block.png'), load_image('purple_block.png'),
              load_image('green_block.png'),load_image('blue_block.png'), load_image('orange_block.png'), load_image('cyan_block.png')]
    for i in range(1, len(blocks)):
        blocks[i] = pygame.transform.smoothscale(blocks[i], (CELL_WIDTH, CELL_HEIGHT))

class Block:
    def __init__(self):
        self.cells = list()
    def rotate(self, direction):
        if direction == ROT_RIGHT:
            cells = [[row[i] for row in matrix[::-1]] for i in range(3)]
        elif direction == ROT_LEFT:
             cells = [[row[2-i] for row in self.cells] for i in range(3)]
        else:
             pass
        if self.boundChecker(topLeft):
             self.cells = cells

    def lowest(self):
        for i in range(len(self.cells)-1, -1, -1):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == 1:
                    return i

    def update(self):
        self.move(DOWN)
        
    def draw(self, screen):
        for i in range(len(self.cells)):
             for j in range(len(self.cells)):
                 if self.cells[i][j] == 1:
                     screen.blit(blocks[self.color], ((self.topLeft[0]+BOARD_OFFSET_X+i)*CELL_WIDTH,
                                                      (self.topLeft[1]+BOARD_OFFSET_Y+j)*CELL_HEIGHT))
    
    def boundChecker(self, temp):
        if not((temp[0]+len(self.cells)-1 >= BOARD_WIDTH and reduce(add, [row[len(self.cells)-1] for row in self.cells]) > 0) or
               (temp[0] < 0 and reduce(add, [row[0] for row in self.cells]) > 0)):
            self.topLeft = temp
            return True
            
               
    def move(self, direction):
        if direction == RIGHT:
            self.boundChecker((self.topLeft[0]+1,self.topLeft[1]))
        elif direction == LEFT:
            self.boundChecker((self.topLeft[0]-1, self.topLeft[1]))
        elif direction == UP:
            self.boundChecker((self.topLeft[0], self.topLeft[1]-1))
        elif direction == DOWN:
            self.boundChecker((self.topLeft[0], self.topLeft[1]+1))
        
    """    
    def move(self, direction):
        if direction == RIGHT:
            if not(self.topLeft+3 > self.xbound[1] and self.cells[2]+self.cells[5]+self.cells[8]>0):
                for cell in self.realCells:
                    cell[0]+=1
        elif direction == LEFT:
            if not(self.topLeft-1 < self.xbound[0] and self.cells[0]+self.cells[3]+self.cells[6]):
                for cell in self.realCells:
                    cell[0]-=1
        elif direction == DOWN:
            for cell in self.realCells:
                cell[1]+=1
    """
        

class L(Block):
    def __init__(self, posx, posy):
        Block.__init__(self)
        self.cells = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.topLeft = (posx, posy)
        self.color = ORANGE
class Square(Block):
    def __init__(self, posx, posy):
        Block.__init__(self)
        self.cells = [[0, 0, 0],[1, 1, 0], [1, 1, 0]]
        self.topLeft = (posx, posy-1)
        self.color = YELLOW
    def rotate(self, direction):
        pass

blockList = [L, Square]
def generate(posx, posy):
    return random.choice(blockList)(posx, posy)
            
        
        
        
        
