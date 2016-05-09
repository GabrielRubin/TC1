#!/usr/bin/env python
# Four spaces as indentation [no tabs]
from __future__ import division

from common import *
from random import choice

from math import log, sqrt

import datetime


# ==========================================
# Player Minimax
# ==========================================

class Player_MonteCarlo:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        self.m_index        = index
        self.m_isHuman      = False
        self.m_isMonteCarlo = True
        self.m_boardHistory = []
        self.wins           = {}
        self.plays          = {}

    def Update(self, board):
        self.m_boardHistory.append(board)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        self.m_maxDepth = 0

        currBoard  = board[:]
        currPlayer = GetCurrentPlayer(currBoard)
        legalMoves = find_empty_cells(currBoard)

        if len(legalMoves) == 0:
            return
        elif len(legalMoves) == 1:
            return legalMoves[0]

        games = 0

        beginTime = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - beginTime < MONTECARLO_MAXTIME:
            self.RunSimulation()
            games += 1

        moveStates = [(m, tuple(GetNextState(currBoard[:], m, currPlayer))) for m in legalMoves]

        print "Total Games: " + str(games), datetime.datetime.utcnow() - beginTime

        percentWins, move = max(((self.wins.get((currPlayer, S), 0)/self.plays.get((currPlayer, S), 1), m) for m, S in moveStates))

        for x in sorted(
            ((100 * self.wins.get((currPlayer, S), 0) /
              self.plays.get((currPlayer, S), 1),
              self.wins.get((currPlayer, S), 0),
              self.plays.get((currPlayer, S), 0), m)
             for m, S in moveStates),
            reverse=True
        ):
            print "{3}: {0:.2f}% ({1} / {2})".format(*x)

        #print "Maximum depth searched:", self.m_maxDepth

        return move

    def RunSimulation(self):
        visitedStates = set()
        historyCopy   = self.m_boardHistory[:]
        currBoard     = historyCopy[-1]
        currPlayer    = GetCurrentPlayer(currBoard)
        expand        = True

        for m in xrange(MONTECARLO_MAXMOVES):
            move      = choice(find_empty_cells(currBoard))
            currBoard = tuple(GetNextState(list(currBoard), move, currPlayer))

            historyCopy.append(currBoard)

            #PrintBoard(list(currBoard))
            #print(m)

            if expand and (currPlayer, currBoard) not in self.plays:
                expand = False
                self.plays[(currPlayer, currBoard)] = 0
                self.wins[(currPlayer, currBoard)]  = 0

            visitedStates.add((currPlayer, currBoard))

            currPlayer = GetCurrentPlayer(currBoard)
            winner     = find_winner(currBoard)
            if winner != None:
                break

        for player, board in visitedStates:
            if(player, board) not in self.plays:
                continue
            self.plays[(player, board)] += 1
            if player == winner:
                self.wins[(player, board)] += 1