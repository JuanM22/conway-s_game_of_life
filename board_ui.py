import pygame
import sys

from board import Board
from cell import Cell

black = (0, 0, 0)
white = (255, 255, 255)
green = [0, 255, 0]
red = (255, 0, 0)
WIDTH = 10
HEIGHT = 10
MARGIN = 1

prevBoard = []
board = []
prevBooleanBoard = []
booleanBoard = []
initPopulation = 0

pygame.init()
resolution = pygame.display.Info()
size = width, height = resolution.current_w, resolution.current_h
scr = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
boardWidth = (resolution.current_w * 65) / 100
boardHeight = (resolution.current_h * 92) / 100

ROWS = int(boardHeight / 10)
COLS = int(boardWidth / 10)

def _createEmptyBoards():
    for row in range(ROWS):
        board.append([])
        prevBoard.append([])
        for _ in range(COLS):
            board[row].append(Cell(False))
            prevBoard[row].append(Cell(False))

    for row in range(ROWS):
        booleanBoard.append([])
        prevBooleanBoard.append([])
        for _ in range(COLS):
            booleanBoard[row].append(False)
            prevBooleanBoard[row].append(False)

pygame.display.set_caption("Conway's Life Game")
clock = pygame.time.Clock()

### FONT ###
pygame.font.init()
dataFont = pygame.font.SysFont('Arial', 15)
#######################

########## PANELS ##########
buttonsPanel = pygame.Surface([(width*25)/100, (height*15)/100])
dataPanel = pygame.Surface([(width*25)/100, (height*15)/100])
####################################

########## CONTROLS ##########

### Start Button ###
startBtn = pygame.image.load('./resources/start_btn.png')
startBtn_rect = startBtn.get_rect()
startBtn_rect.x = (width*2)/100
startBtn_rect.y = (height*2)/100
#########################################

### Restart Button ###
restartBtn = pygame.image.load('./resources/restart_btn.png')
restartBtn_rect = restartBtn.get_rect()
restartBtn_rect.x = (width*7)/100
restartBtn_rect.y = (height*2)/100
#########################################

### Clear Button ###
clearBtn = pygame.image.load('./resources/clear_btn.png')
clearBtn_rect = clearBtn.get_rect()
clearBtn_rect.x = (width*2)/100
clearBtn_rect.y = (height*7)/100
#########################################

########## DATA LABELS ##########
generationText = dataFont.render('Generation >>>', False, green)
populationText = dataFont.render('Population  >>>', False, green)
#########################################

_createEmptyBoards()

boardInstance = Board(board, booleanBoard)
isPlaying = False
isRunning = True
isEditing = True
clockTick = 50

def _renderPanel():
    _renderButtonsPanel()
    _renderDataPanel()

def _renderButtonsPanel():
    buttonsPanel.fill(white)
    buttonsPanel.blit(startBtn, [startBtn_rect.x, startBtn_rect.y])
    buttonsPanel.blit(restartBtn, [restartBtn_rect.x, restartBtn_rect.y])
    buttonsPanel.blit(clearBtn, [clearBtn_rect.x, clearBtn_rect.y])
    scr.blit(buttonsPanel, [(width * 72) /100, (height * 2) /100])
    scr.blit(dataPanel, [(width * 72) /100, (height * 25) /100])


def _renderDataPanel():
    dataPanel.fill(black)
    dataPanel.blit(generationText, [(width * 2) /100, (height * 2) /100])
    dataPanel.blit(populationText, [(width * 2) /100, (height * 6) /100])
    #### Updated Data ####
    generationValue = dataFont.render(str(boardInstance.generationCounter), False, green)
    populationValue = dataFont.render(str(boardInstance.population), False, green)
    dataPanel.blit(generationValue, [(width * 10) /100, (height * 2) /100])
    dataPanel.blit(populationValue, [(width * 10) /100, (height * 6) /100])

def _editCells(mousePos, initPopulation, button):
    col = mousePos[0] // (WIDTH + MARGIN)
    row = mousePos[1] // (HEIGHT + MARGIN)
    if((row >=0 and row < ROWS) and (col >= 0 and col < COLS)):
        if(not(prevBooleanBoard[row][col]) and button == 1):    
            ## Carga tableros previos en caso de reiniciar la simulación ##
            prevBoard[row][col].state = True
            prevBooleanBoard[row][col] = True
            ###############################################################
            ## Carga tableros para la simulación ##
            boardInstance.board[row][col].state = True
            boardInstance.booleanBoard[row][col] = True
            ###############################################################
            initPopulation += 1
        elif(prevBooleanBoard[row][col] and button == 2):
            ## Carga tableros previos en caso de reiniciar la simulación ##
            prevBoard[row][col].state = False
            prevBooleanBoard[row][col] = False
            ###############################################################

            ## Carga tableros para la simulación ##
            boardInstance.board[row][col].state = False
            boardInstance.booleanBoard[row][col] = False
            ###############################################################
            initPopulation -= 1

        boardInstance.population = initPopulation
        
    return initPopulation

while isRunning:

    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if(event.button == 1):
                ### Button event handlers ###
                if startBtn_rect.collidepoint([mpos[0] - (width* 72)/100, mpos[1] - (height * 2)/100]):
                    if(initPopulation > 0):
                        isPlaying = True
                        isEditing = False
                        boardInstance.population = initPopulation ## Asigna la población inicial ###
                elif restartBtn_rect.collidepoint([mpos[0] - (width* 72)/100, mpos[1] - (height * 2.1)/100]):
                    isEditing = True
                    isPlaying = False
                    boardInstance.population = initPopulation ## Asigna la población inicial ###
                    boardInstance.board = prevBoard ## Asigna el tablero inicial ###
                    boardInstance.booleanBoard = prevBooleanBoard ## Asigna el tablero de booleanos inicial ###
                    boardInstance.generationCounter = 0
                elif clearBtn_rect.collidepoint([mpos[0] - (width* 72.05)/100, mpos[1] - (height * 2.1)/100]):
                    isEditing = True
                    isPlaying = False
                    board = []
                    booleanBoard = []
                    prevBoard = []
                    prevBooleanBoard = []
                    _createEmptyBoards() ## Reinicia los tableros
                    boardInstance.board = board
                    boardInstance.booleanBoard = booleanBoard
                    boardInstance.population = 0
                    boardInstance.generationCounter = 0
                    initPopulation = 0
        elif pygame.mouse.get_pressed()[0]: ## Mouse holding down
            mpos = pygame.mouse.get_pos()
            if(isEditing):
                ### Cell activation ###
                initPopulation = _editCells(mpos, initPopulation, 1)
                ###############################
        elif pygame.mouse.get_pressed()[2]: ## Mouse holding down
            mpos = pygame.mouse.get_pos()
            if(isEditing):
                ### Cell activation ###
                initPopulation = _editCells(mpos, initPopulation, 2)
                ###############################

    if(isPlaying):
        boardInstance.updateCells()
        isPlaying = boardInstance.isAnyOneAlive()

    scr.fill(black)
    _renderPanel()

    for row in range(ROWS):
        for column in range(COLS):
            color = white
            if(boardInstance.booleanBoard[row][column]):
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    

    clock.tick(clockTick)
    pygame.display.flip()