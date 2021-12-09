from numpy import *

from cell import Cell
from board import Board

booleanBoard = array([
    [False, True, False, False], 
    [True, True, True, True], 
    [False, True, True, False], 
    [True, True, False, True], 
])

board  = array([
    [Cell(False,'D'), Cell(True,'A'), Cell(False,'D'), Cell(False,'D')],
    [Cell(True,'A'), Cell(True,'A'), Cell(True,'A'), Cell(True,'A')],
    [Cell(False,'D'), Cell(True,'A'), Cell(True,'A'), Cell(False,'D')],
    [Cell(True,'A'), Cell(False,'D'), Cell(False,'D'), Cell(True,'A')]
])

simulation = Board(0, board, booleanBoard)

def printBoard(board):
    for i in range(0,len(board)): # Número de filas #
        for j in range(0, len(board[i])): # Número de columnas #
            print(board[i][j].icon, ' ', end='')
        print()

printBoard(simulation.board)

print('\n', end='\r')

while(simulation.isAnyOneAlive()):
    simulation.updateCells()
    printBoard(simulation.board)
    print('\n', end='\r')

