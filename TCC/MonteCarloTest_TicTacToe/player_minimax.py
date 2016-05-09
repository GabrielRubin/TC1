#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from common import *

# ==========================================
# Player Minimax
# ==========================================

class Player_Minimax:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        self.m_index        = index
        self.m_isHuman      = False
        self.m_isMonteCarlo = False

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        # TODO
        return None