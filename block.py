import pygame
blockList = [L, Square] 
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
        if boundChecker(topLeft):
             self.cells = cells
             
    def update(self):
        self.move(DOWN)
        
    def draw(self, screen):
        for i in range(len(self.cells)):
             for j in range(len(self.cells)):
                 if self.cells[i][j] == 1:
                     screen.blit(blocks[self.color], ((topLeft[0]+i)*CELL_WIDTH,(topLeft[1]+j)*CELL_HEIGHT))


    def add(x, y):
        return x + y
    
    def boundChecker(self, temp):
        if not(temp[0]+len(self.cells)-1 >= BOARD_WIDTH and reduce(add, [row[len(self.cells)-1] for row in self.cells]) > 0 or
               temp[0] < 0 and reduce(add, [row[0] for row in self.cells]) > 0):
            self.topLeft = temp
            return True
            
               
    def move(self, direction):
        if direction == RIGHT:
            boundChecker((self.topLeft[0]+1,self.topLeft[1]))
        elif direction == LEFT:
            boundChecker((self.topLeft[0]-1, self.topLeft[1]))
        elif direction == UP:
            boundChecker((self.topLeft[0], self.topLeft[1]-1))
        elif direction == DOWN:
            boundChecker((self.topLeft[0], self.topLeft[1]+1))
        
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
    def generate(posx, posy):
        return random.choice(blockList)(posx, posy)
        

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

    
    
   
                                                
            
        
        
        
        
