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
    def __init__(self, posx, posy):
        self.cells = list()
        self.topLeft = (posx, posy)
    def rotate(self, direction):
        if direction == ROT_RIGHT:
            newCells = [[row[i] for row in self.cells[::-1]] for i in range(3)]
        elif direction == ROT_LEFT:
            newCells = [[row[2-i] for row in self.cells] for i in range(3)]
        else:
             pass
        if self.boundChecker(self.topLeft, newCells):
            self.cells = newCells

    def lowest(self):
        for i in range(len(self.cells)-1, -1, -1):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == 1:
                    return i+self.topLeft[1]

    def update(self):
        self.move(DOWN)
        
    def draw(self, screen, posx, posy):
        for i in range(len(self.cells)):
             for j in range(len(self.cells)):
                 if self.cells[j][i] == 1:
                     screen.blit(blocks[self.color], ((self.topLeft[0]+posx+i)*CELL_WIDTH,
                                                      (self.topLeft[1]+posy+j)*CELL_HEIGHT))
    
    def boundChecker(self, temp, cells):
        if not((temp[0]+len(cells)-1 >= BOARD_WIDTH and reduce(add, [row[len(self.cells)-1] for row in cells]) > 0) or
               (temp[0]+len(cells)-2 >= BOARD_WIDTH and reduce(add, [row[len(self.cells)-2] for row in cells]) > 0) or
               (temp[0]+len(cells)-3 >= BOARD_WIDTH and reduce(add, [row[len(self.cells)-3] for row in cells]) > 0) or
               (temp[0] < 0 and reduce(add, [row[0] for row in cells]) > 0) or
               (temp[0] + 1 < 0 and reduce(add, [row[1] for row in cells]) > 0) or
               (temp[0] + 2 < 0 and reduce(add, [row[2] for row in cells]) > 0)):
            self.topLeft = temp
            return True
        return False
            
               
    def move(self, direction):
        if direction == RIGHT:
            self.boundChecker((self.topLeft[0]+1,self.topLeft[1]), self.cells)
        elif direction == LEFT:
            self.boundChecker((self.topLeft[0]-1, self.topLeft[1]), self.cells)
        elif direction == UP:
            self.boundChecker((self.topLeft[0], self.topLeft[1]-1), self.cells)
        elif direction == DOWN:
            self.boundChecker((self.topLeft[0], self.topLeft[1]+1), self.cells)
        
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
        

class J(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy)
        self.cells = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.color = BLUE
class Square(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy-1)
        self.cells = [[0, 0, 0],[1, 1, 0], [1, 1, 0]]
        self.color = YELLOW
    def rotate(self, direction):
        pass
class L(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy-1)
        self.cells = [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
        self.color = ORANGE
class T(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy-1)
        self.cells = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]
        self.color = PURPLE

class Z(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy)
        self.cells = [[1, 1, 0], [0, 1, 1], [0, 0, 0]]
        self.color = RED
class S(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy-1)
        self.cells = [[0, 1, 1], [1, 1, 0], [0, 0, 0]]
        self.color = GREEN
class I(Block):
    def __init__(self, posx, posy):
        Block.__init__(self, posx, posy-1)
        self.cells = [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
        self.color = CYAN
    def 
        
blockList = [L, Square, J, T, Z, S]
def generate(posx, posy):
    return random.choice(blockList)(posx, posy)
            
        
        
        
        
