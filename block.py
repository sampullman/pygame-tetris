import pygame

class Block:
    def __init__(self, bounds):
        self.cells = list()
        self.xbound = (bounds[0], bounds[1])
        self.ybound = (bounds[2], bounds[3])
    def rotate(self, direction):
        pass
    def update(self):
        pass
    def draw(self):
        
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

class L(Block):
    def __init__(self, posx, posy):
        Block.__init__(self)
        self.cells = [0, 0, 0, 1, 1, 1, 1, 0, 0]
        self.topLeft = (posx, posy-1)
        self.color = ORANGE

    def rotate(self, direction):
        if direction == ROT_RIGHT:
            cells = [self.cells[6],self.cells[3],self.cells[0],self.cells[7],...
                     self.cells[4],self.cells[1], self.cells[8], self.cells[5],...
                     self.cells[2]]
            if not((self.topLeft[0] < self.xbound[0] and (cells[0]+cells[3]+cells[6] > 0)) or ...
                   (self.topLeft[0]+2 > self.xbound[1] and (cells[2]+cells[5]+cells[8] > 0))):
                self.cells = cells
                self.realCells = []
                i = 0
                for cell in self.cells:
                    if cell == 1:
                        self.realCells += [(self.
   
                                                
            
        
        
        
        
