#Name - Piyush Joshi
#Subject - Python for Analytics
#Submitted To - Prof. Himanshu Ramchandani
#Topic - TicTacToe

import pygame,sys #for screen
import numpy as np #for console 

pygame.init() #we are initialising pygame

WIDTH = 700
HEIGHT = WIDTH 
LINE_WIDTH=15
WIN_LINE_WIDTH=15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE=WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4 #space between line and corner

#create colour as constant
BG_COLOR=(251,232,96)
LINE_COLOR=(248,160,44)
CIRCLE_COLOR=(58,88,228)
CROSS_COLOR = (251,68,36)

screen=pygame.display.set_mode((WIDTH, HEIGHT)) #we pass height and width of screen
#when this is runned a file comes and goes and it doesn't stay as we don't have a main loop
#Pygame loop is always the same 
pygame.display.set_caption('TIC_TAC_TOE by Piyush Joshi')
screen.fill(BG_COLOR)# we will use the RGB scheme (red,green,blue)
# When we run the file with just red the screen will not change as we have not updated

#Console Board
board = np.zeros((BOARD_ROWS,BOARD_COLS))
# print(board)


# pygame.draw.line( screen, RED, (10,10),(300,300),10)#screen,color of line, start and end, width
def draw_lines():
    #1st Horizontal
    pygame.draw.line(screen,LINE_COLOR,(0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)
    #2nd Horizontal
    pygame.draw.line(screen,LINE_COLOR,(0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE),LINE_WIDTH)
    #1st Vertical
    pygame.draw.line(screen,LINE_COLOR,(SQUARE_SIZE,0),(SQUARE_SIZE,HEIGHT),LINE_WIDTH)
    #2nd Vertical
    pygame.draw.line(screen,LINE_COLOR,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,HEIGHT),LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*SQUARE_SIZE +SQUARE_SIZE//2),int(row*SQUARE_SIZE+SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),CROSS_WIDTH)
#functions for  board mark square to mark them
def mark_square(row,col,player):#marks the square
    board[row][col]=player
def available_square(row,col):#is the square available or not
    # return board[row][col]==0 (Same as below two lines)
    if board[row][col]==0:
        return True
    else:
        return False
def is_board_full():#we won't receive any parameters, will give true if its full
    #go to each square are you available
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return True
def check_win(player):
    # check vertical win loop by loop through 3 column 
    # check horizontal win loop by loop through 3 rows
    # check both diagonal manually
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_wining_line(col,player)
            return True #by returning true we are breaking the function and break the process
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    #asc diagonal win check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    #desc diagonal win check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True
    return False #case of no win
        
def draw_vertical_wining_line(col,player):
    posX = col*SQUARE_SIZE + SQUARE_SIZE//2
    if player ==1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),WIN_LINE_WIDTH)

def draw_horizontal_winning_line(row,player):
    posY = row*SQUARE_SIZE+SQUARE_SIZE//2
    if player ==1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR
         
    pygame.draw.line( screen,color,(15,posY),(WIDTH-15,posY),WIN_LINE_WIDTH)

def draw_asc_diagonal(player):
    if player ==1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),WIN_LINE_WIDTH)

def draw_desc_diagonal(player):
    if player ==1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),WIN_LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0
# print(is_board_full()) #board not full so its False
# for row in range(BOARD_ROWS):
#         for col in range(BOARD_COLS):
#             mark_square(row,col,1)
# print(is_board_full()) #as board is now full it returns True

#is the middle squre available???
# print(available_square(1,1))
# mark_square(1,1,2)
# print(available_square(1,1))
# mark_square(0,0,1)
# mark_square(1,1,2)
# print(board)
draw_lines()
#mainloop, might seems confusing but it is common in all lanaguages

player = 1
game_over=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y
            # print(mouseX) #it prints the coordinate of clicking
            # print(mouseY)
            clicked_row = int(mouseY//SQUARE_SIZE) #reduce the 600 pixels to 0,1,2
            clicked_col = int(mouseX//SQUARE_SIZE)
            # print(clicked_row)
            # print(clicked_col)

            if available_square(clicked_row,clicked_col):
                if player ==1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over=True
                    player =2
                elif player ==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over=True
                    player=1 #update the player
                    #player=player%2+1
                # print(board)
                #screen board to console linked
                #now we need to create function to draw figures
                draw_figures()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                player=1
                game_over=False

    pygame.display.update()
    #pygame coordinates, the coordinates  work as fourth quadrant origin upper left corner
    #lower side (600,600)
