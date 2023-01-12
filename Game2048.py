
#--Build 2048 in python using pygame
import pygame
import random

pygame.init()

#--Initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesambold.ttf', 24)

#--2048 game colo library
color = {0: (204, 192, 179),
         2: (238, 228, 218),
         4: (237, 224, 200),
         8: (242, 177, 121),
         16: (245, 149, 99),
         32: (246, 124, 95),
         64: (246, 94, 59),
         128: (237, 207, 114),
         256: (237, 204, 97),
         512: (237, 200, 80),
         1024: (237, 197, 63),
         2048: (237, 194, 46),
         'light text' : (249, 246, 242),
         'dark tex' : (119, 110, 101),
         'other' : (0, 0, 0,),
         'bg' : (187, 173, 160)}

#--Game variable initialize
board_value = [[0 for _ in range(4)] for _  in range(4)]
game_over = False
spawn_new = True 
init_count = 0
direction = ''
score = 0
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high

#--Draw game over and restart text
def draw_over():
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2  = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))
    
#--Take your turn based on direction
def take_turn(direc, board):
    global score
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                        if shift > 0:
                            board[i - shift][j] = board[i][j]
                            board[i][j] = 0
                        if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift - 1][j] \
                            and not merged[i - shift - 1][j]:
                            board[i - shift - 1][j] *= 2
                            score += board[i - shift - 1][j]
                            board[i - shift][j] = 0
                            merged[i - shift - 1][j] = True
                            
    elif direc == 'DOWN':
        for i in range(3):
            for j in range (4):
                shift = 0
                for i in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                    if shift > 0:
                        board[2 - i + shift][j] = board[2 - i][j]
                        board[2 -i][j] = 0
                    if 3 - i + shift <= 3:
                        if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3  - i + shift][j] and not merged[2 - i + shift][j]:
                            board[3 - i + shift][j] *= 2
                            score += board[3 - i + shift][j]
                            board[2 - i + shift][j] = 0
                            merged[i][j - shift -1] = True
    
    elif direc == 'LEFT': 
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j] - shift == board[i][j - 1] and not merged[i][j - shift - 1] \
                    and not merged[i][j - shift]:
                        board[i][j - shift - 1] *= 2
                        score += board[i][j - shift - 1]
                        board[i][j - shift] = 0
                        merged[i][j - shift - 1] = True


    elif direc == 'RIGHT':
        for i in range(4):
            for i in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] \
                        and not merged[i][3 - j + shift]:
                            board[i][4 - j + shift] *= 2
                            score += board[i][4 - j + shift]
                            board[i][3 - j + shift] = 0
                            merged[i][4 - j + shift] = True
    return board

#--Spawn in new pieces randomly when turns start


