#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import sys


# In[5]:


#initialize pygame
pygame.init()
pygame.font.init()


# In[6]:


#constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE//4

#Colors
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (100, 100, 100)
CROSS_COLOR = (200, 0, 0)


# In[7]:


def draw_grid():
    #horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0,SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2), LINE_WIDTH)

    #vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*2,0), (SQUARE_SIZE*2,HEIGHT), LINE_WIDTH)


# In[1]:


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                #draw a circle
                pygame.draw.circle(screen, CIRCLE_COLOR, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                
            elif board[row][col]:
                #draw a cross
                font = pygame.font.SysFont("arial",45)
                text_surface = font.render("X", True, CROSS_COLOR)
                text_rect = text_surface.get_rect(center = (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2))
                screen.blit(text_surface, text_rect)


# In[9]:


def mark_square(row,col,player):
    board[row][col] = player


# In[10]:


def available_square(row,col):
    return board[row][col]==0


# In[11]:


def is_board_full():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True


# In[12]:


def check_win(player):
    #check rows, cols and diagonals
    for row in range(BOARD_ROWS):
        if  all([cell == player for cell in board[row]]):
            return True

    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True

    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True

    if all([board[i][BOARD_ROWS -1 -i]  == player for i in range(BOARD_ROWS)]):
        return True
    return False


# In[ ]:


def restart():
    global board, player
    board = [[0]*BOARD_COLS for _ in range(BOARD_ROWS)]
    screen.fill(BG_COLOR)
    


# In[13]:


#setting up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

board = [[0]*BOARD_COLS for _ in range(BOARD_ROWS)]

draw_grid()
player = 1
game_over = False

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0]  # X coordinate 
            mousey = event.pos[1]  # Y coordinate

            clicked_row = mousey // SQUARE_SIZE
            clicked_col = mousex // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    print(f"Player {player} wins!")
                    game_over = True
                player = player%2 + 1 #switching the player

                draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
    pygame.display.update()


# In[ ]:





# In[ ]:




