#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import time
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_SPACE)
from tictactoe import *

# ==========================================
# Interface
# ==========================================

class Interface:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, playerO, playerX):
        # Setup
        pygame.init()
        self.screen = pygame.display.set_mode((TILE_WIDTH * 3, TILE_HEIGHT * 3))
        pygame.display.set_caption("[T1b]   Tic-Tac-Toe")
        self.load_tileset("tiles.bmp", 3, 1)
        self.game = TicTacToe(playerO, playerX)
        self.draw_board()
        pygame.display.flip()
        # Loop
        time_passed = 0
        game_over = False
        while not game_over:
            # Update every WAIT seconds
            if self.game.playerO.m_isHuman or self.game.playerX.m_isHuman:
                self.game.update()
                self.draw_board()
            else:
                if time.time() - time_passed > WAIT:
                    self.game.update()
                    self.draw_board()
                    time_passed = time.time()
            # Events
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE: # Reset game
                        print "Reset board"
                        self.board = [0 for i in range(9)]
                        self.turn = 1
                        self.game = TicTacToe(playerO, playerX)
                        self.draw_board()

    # ------------------------------------------
    # Draw board
    # ------------------------------------------

    def draw_board(self):
        index = 0
        board_y = 0
        for row in range(3):
            board_x = 0
            for cell in range(3):
                self.screen.blit(self.tileset[self.game.board[index]], (board_x, board_y))
                index += 1
                board_x += TILE_WIDTH
            board_y += TILE_HEIGHT

    # ------------------------------------------
    # Load image
    # ------------------------------------------

    def load_image(self, filename):
        img = pygame.image.load(os.path.join(PATH, "sprites", filename)).convert()
        if ZOOM > 1:
            return pygame.transform.scale(img, (img.get_width() * ZOOM, img.get_height() * ZOOM))
        return img

    # ------------------------------------------
    # Load tileset
    # ------------------------------------------

    def load_tileset(self, filename, width, height):
        image = self.load_image(filename)
        self.tileset = []
        tile_y = 0
        for y in range(height):
            tile_x = 0
            for x in range(width):
                self.tileset.append(image.subsurface((tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)))
                tile_x += TILE_WIDTH
            tile_y += TILE_HEIGHT

# ==========================================
# Main
# ==========================================
if __name__ == "__main__":
    if len(sys.argv) == 3:
        playerO = int(sys.argv[1])
        playerX = int(sys.argv[2])
    else:
        print "Loading default random players"
        playerO = RANDOM
        playerX = MONTECARLO
    Interface(playerO, playerX)