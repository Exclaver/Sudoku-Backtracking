import os, sys
import pygame
import time
from sudoku_game_logic import *
from pygame.locals import *


def draw_sudoku():
    """
    Draws the Sudoku grid on the screen using Pygame.
    """
    # pygame.draw.rect(screen, BLACK, [screen.get_width() // 2 // 5, screen.get_height() // 2 // 6, 452, 452], 4)
    # Draw horizontal lines
    line_width = 2
    line_count = 0
    for i in range(0, 500, 50):
        line_count %= 3
        if line_count == 0:
            line_width = 4
        else:
            line_width = 2
        line_count += 1

        pygame.draw.line(screen, BLACK, [screen.get_width() // 2 // 5, screen.get_height() // 2 // 6 + i],
                         [screen.get_width() // 2 // 5 + 450, screen.get_height() // 2 // 6 + i], line_width)

    # Draw vertical lines
    line_count = 0
    for i in range(0, 500, 50):
        line_count %= 3
        if line_count == 0:
            line_width = 4
        else:
            line_width = 2
        line_count += 1

        pygame.draw.line(screen, BLACK, [screen.get_width() // 2 // 5 + i, screen.get_height() // 2 // 6],
                         [screen.get_width() // 2 // 5 + i, screen.get_height() // 2 // 6 + 450], line_width)


def event_handler():
    """
    Handles events such as quitting the game.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


def draw_number(x, y, text):
    """
    Draws a number on the Sudoku grid.

    Args:
    x (int): X-coordinate of the number's position.
    y (int): Y-coordinate of the number's position.
    text (str): The number to be drawn.
    """
    font = pygame.font.SysFont('Calibri', 35)
    text_surf = font.render(str(text), True, BLACK)
    screen.blit(text_surf, [x, y])


# Update Surface
def screen_update():
    """
    Updates the screen in Pygame.
    """
    pygame.display.flip()
    pygame.display.update()


def drawArray(arr):
    """
    Draws the numbers from the Sudoku puzzle array onto the grid.

    Args:
    arr (list of lists): 2D list representing the Sudoku puzzle.
    """
    i = 0
    j = 0
    for x in range(screen.get_width() // 2 // 5, screen.get_width() // 2 // 5 + 400 + 30, 50):
        i = 0
        for y in range(screen.get_height() // 2 // 6, screen.get_height() // 2 // 6 + 400 + 30, 50):
            if arr[i][j] > 0:
                draw_number(x + 17, y + 11, arr[i][j])
            i += 1
        j += 1


def draw_update(arr):
    """
    Redraws the entire game screen including the Sudoku grid and the current state of the puzzle.

    Args:
    arr (list of lists): 2D list representing the current state of the Sudoku puzzle.
    """
    event_handler()
    screen.fill(WHITE)
    draw_sudoku()
    drawArray(arr)
    screen_update()


def solver(arr, i=0, j=0):
    """
    Solves the Sudoku puzzle using a backtracking algorithm.

    Args:
    arr (list of lists): 2D list representing the Sudoku puzzle.
    i (int): Current row index.
    j (int): Current column index.

    Returns:
    list of lists: Solved Sudoku puzzle or None if no solution exists.
    """
    if j == 9:
        return solver(arr, i + 1, 0)
    if i == 9:
        return arr
    if arr[i][j] != 0:
        return solver(arr, i, j + 1)
    for x in range(1, 10):
        draw_update(arr)
        if valid_move(x, i, j, arr):
            arr[i][j] = x
            draw_update(arr)
            # time.sleep(0.25)

            if solver(arr, i, j + 1) is not None:
                return arr
            arr[i][j] = 0
    # time.sleep(0.25)
    return None

# Initialization and main loop
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound ')

# RGB - Colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# Init Pygame and Font
pygame.init()
pygame.font.init()

# Create Window
(width, height) = (560, 550)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku Solver')

# Sudoku puzzle initialization
sudoku = [    [0, 0, 0, 0, 4, 0, 6, 1, 3],
              [0, 0, 0, 7, 0, 8, 0, 4, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],

              [3, 5, 0, 1, 0, 0, 0, 0, 7],
              [1, 0, 0, 0, 3, 0, 0, 0, 9],
              [4, 0, 0, 0, 0, 2, 0, 3, 1],

              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 4, 0, 2, 0, 7, 0, 0, 0],
              [7, 1, 2, 0, 6, 0, 0, 0, 0]]

# Main loop
# Sudoku Overlay
screen.fill(WHITE)
draw_sudoku()
drawArray(sudoku)
solver(sudoku)

while True:
    event_handler()
    screen_update()
