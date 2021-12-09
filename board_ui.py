import pygame
import sys
black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
WIDTH = 6
HEIGHT = 6
MARGIN = 1
grid = []

pygame.init()
resolution = pygame.display.Info()
size = width, height = (resolution.current_w * 65) / 100, resolution.current_h
scr = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

ROWS = int(height / 6)
COLS = int(width / 6)

print(width)

for row in range(ROWS):
    grid.append([])
    for column in range(COLS):
        grid[row].append(0) 

pygame.display.set_caption("Conway's Life Game")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if((row >=0 and row < ROWS) and (col >= 0 and col < COLS)):
                if(grid[row][col] == 1):
                    grid[row][col] = 0
                else:
                    grid[row][col] = 1
                print("Click ", pos, "Grid coordinates: ", row, col)
    scr.fill(black)
    for row in range(ROWS):
        for column in range(COLS):
            color = white
            if grid[row][column] == 1:
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(50)
    pygame.display.flip()
pygame.quit()