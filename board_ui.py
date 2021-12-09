import pygame
import sys

from board import Board
from cell import Cell

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
WIDTH = 10
HEIGHT = 10
MARGIN = 1
board = []
booleanBoard = []

pygame.init()
resolution = pygame.display.Info()
size = width, height = (resolution.current_w * 65) / 100, resolution.current_h
scr = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

ROWS = int(height / 10)
COLS = int(width / 10)

for row in range(ROWS):
    board.append([])
    for column in range(COLS):
        board[row].append(Cell(False,'D'))

for row in range(ROWS):
    booleanBoard.append([])
    for column in range(COLS):
        booleanBoard[row].append(False)

pygame.display.set_caption("Conway's Life Game")
clock = pygame.time.Clock()

boardInstance = Board(board, booleanBoard)
isPlaying = False
isRunning = True
clockTick = 50

while isRunning:

    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
            if(event.key == pygame.K_SPACE):
                isPlaying = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(not(isPlaying)):
                pos = pygame.mouse.get_pos()
                col = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if((row >=0 and row < ROWS) and (col >= 0 and col < COLS)):
                    boardInstance.board[row][col] = Cell(True, 'A') if(not(boardInstance.board[row][col].state)) else Cell(False, 'D')
                    boardInstance.booleanBoard[row][col] = True if(boardInstance.board[row][col] == None) else False

    scr.fill(black)

    if(isPlaying):
        boardInstance.updateCells()
        isRunning = boardInstance.isAnyOneAlive()

    for row in range(ROWS):
        for column in range(COLS):
            color = white
            if(boardInstance.board[row][column].state):
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(clockTick)
    pygame.display.flip()
pygame.quit()