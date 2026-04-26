import random
from os import system

def start_game():
    return [[0 for _ in range(3)] for _ in range(3)]
def board_state(board):
    # check for win
    for row in board:
        if row[0]==row[1]==row[2]!=0:
            return row[0]
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]!=0:
            return board[0][col]
    if board[0][0]==board[1][1]==board[2][2]!=0:
        return board[0][0]
    if board[2][0]==board[1][1]==board[0][2]!=0:
        return board[1][1]
    # check if game is still going on
    for row in board:
        for num in row:
            if num==0:
                return 0
    # return tie
    return -1
def player_move(board,sym):
    row,col=[int(x) for x in input().split()]
    while board[row][col]!=0:
        row, col = [int(x) for x in input().split()]
    board[row][col]=sym
    return board
def print_board(board):
    for x in board:
        print(*x)


from minimax import *
def ai_move(board, sym):
    best_score=-3
    best_move=None
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                board[row][col]=sym
                sc=MiniMax(board,True,sym,1)
                board[row][col]=0
                best_score,best_move=(best_score,best_move) if best_score>=sc else (sc,(row,col))
    board[best_move[0]][best_move[1]] = sym
    return board,best_move



