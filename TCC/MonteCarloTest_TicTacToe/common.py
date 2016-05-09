#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import os, inspect, datetime

PATH          = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
WAIT          = 1
# Board
ZOOM          = 6
TILE_WIDTH    = 16 * ZOOM
TILE_HEIGHT   = 16 * ZOOM
# Modes
HUMAN         = 0
RANDOM        = 1
MINIMAX       = 2
ALPHABETA     = 3
MONTECARLO    = 4
# Index symbol
O = 1
X = 2
DRAW = 0
# Monte Carlo Options
MONTECARLO_MAXMOVES = 1000
MONTECARLO_MAXTIME  = datetime.timedelta(seconds=1) #seconds

FIRST_PLAYER = O

# ------------------------------------------
# Find winner
# ------------------------------------------

def find_winner(board):
    # Rows
    if board[0] and board[0] == board[1] and board[1] == board[2]:
        return board[0]
    elif board[3] and board[3] == board[4] and board[4] == board[5]:
        return board[3]
    elif board[6] and board[6] == board[7] and board[7] == board[8]:
        return board[6]
    # Columns
    elif board[0] and board[0] == board[3] and board[3] == board[6]:
        return board[0]
    elif board[1] and board[1] == board[4] and board[4] == board[7]:
        return board[1]
    elif board[2] and board[2] == board[5] and board[5] == board[8]:
        return board[2]
    # Diagonals
    elif board[0] and board[0] == board[4] and board[4] == board[8]:
        return board[0]
    elif board[2] and board[2] == board[4] and board[4] == board[6]:
        return board[2]
    elif board.count(0) == 0:
        return 0
    return None

# ------------------------------------------
# Find empty cells
# ------------------------------------------

def find_empty_cells(board):
    return [index for index in range(9) if board[index] == 0]

def GetBoardInitialState():
    return [0 for i in range(9)]

def PrintBoard(board):
    print("--------------------------------")
    for row in [0,3,6]:
        print [' OX'[cell] for cell in board[row:(row+3)]]

def GetNextState(board, move, player):
    board[move] = player
    return board

def GetCurrentPlayer(board):
    x = board.count(X)
    o = board.count(O)
    if FIRST_PLAYER == O:
        if o == x:
            return O
        else:
            return X
    else:
        if x == o:
            return X
        else:
            return O