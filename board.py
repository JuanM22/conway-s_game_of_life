from cell import Cell

class Board:

    def __init__(self, board, booleanBoard):
        self.board = board
        self.booleanBoard = booleanBoard
        self.generationCounter = 0
        self.population = 0

    def updateCells(self):
        for i in range(0,len(self.booleanBoard)): # Número de filas #
            for j in range(0, len(self.booleanBoard[i])): # Número de columnas #
                row = i if(i - 1 < 0) else (i-1)
                col = j if(j - 1 < 0) else (j-1)
                cell = self.board[i][j]
                prevState = cell.state ## Estado previo ##
                if(cell.state):
                    self.booleanBoard[i][j] = self._ifCellIsAlive(i, j, row, col)
                else:
                    self.booleanBoard[i][j] = self._ifCellIsDead(i, j, row, col)
                if(not(prevState) and self.booleanBoard[i][j]):
                    self.population += 1
                
                if(prevState and not(self.booleanBoard[i][j])):
                    self.population -= 1
                
        for i in range(0,len(self.booleanBoard)): # Número de filas #
            for j in range(0, len(self.booleanBoard[i])): # Número de columnas #
                self.board[i][j].state = self.booleanBoard[i][j]
        
        self.generationCounter += 1
        

    # Recorrer vecinos, si tiene más de tres muere la célula
    def _ifCellIsAlive(self, x, y, row, col):
        neighbors = 0
        rowLength = row + self._rowLength(x)
        colLength = col + self._colLength(y)
        for i in range(row, rowLength):
            for j in range(col, colLength):
                if(i != x or j != y):
                    if(self.board[i][j].state):
                        neighbors += 1
        return False if(neighbors > 3 or neighbors < 2) else True # Celula sobrevive

    # Recorrer vecinos, si tiene tres nace la célula
    def _ifCellIsDead(self, x, y, row, col):
        neighbors = 0
        rowLength = row + self._rowLength(x)
        colLength = col + self._colLength(y)
        for i in range(row, rowLength):
            for j in range(col, colLength):
                if(i != x or j != y):
                    if(self.board[i][j].state):
                        neighbors += 1
        return True if(neighbors == 3) else False # Celula nace

    def _rowLength(self, x):
        rowLength = 3
        if(x - 1 < 0):
            rowLength -=1
        if(x + 1 > (len(self.board)-1)):
            rowLength -=1
        return rowLength

    def _colLength(self, y):
        colLength = 3
        if(y - 1 < 0):
            colLength -=1
        if(y + 1 > (len(self.board[0])-1)):
            colLength -=1
        return colLength

    def isAnyOneAlive(self):
        for i in range(0,len(self.board)): # Número de filas #
            isAlive = list(filter(lambda cell: cell.state, self.board[i]))
            if(len(isAlive) > 0):
                return True
        return False