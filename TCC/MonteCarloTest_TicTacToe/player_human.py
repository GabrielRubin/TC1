#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from common import *
import pygame

# ==========================================
# Player Human
# ==========================================

class Player_Human:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        self.m_index        = index
        self.m_isHuman      = True
        self.m_isMonteCarlo = False

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        empty_cells = find_empty_cells(board)
        if pygame.mouse.get_focused() and pygame.mouse.get_pressed()[0]:
            mousePosition = pygame.mouse.get_pos()
            move     = self.GetBoardPosition(mousePosition)
            if move in empty_cells:
                return move

        return None

    def GetBoardPosition(self, position):
        x            = position[0] / TILE_WIDTH
        y            = position[1] / TILE_HEIGHT
        return (y * 2 + x) + (y * 1)
