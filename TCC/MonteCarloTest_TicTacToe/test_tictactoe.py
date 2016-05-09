#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import unittest
from common import *
from tictactoe import *

PLAYS = 10

def percentage(wins, games):
    return float(wins) / float(games) * 100

# ==========================================
# Test TicTacToe
# ==========================================

class Test_TicTacToe(unittest.TestCase):

    # ------------------------------------------
    # Setup
    # ------------------------------------------

    @classmethod
    def setUpClass(cls):
        cls.minimax_vs_random_results = None
        cls.random_vs_minimax_results = None

    @classmethod
    def tearDownClass(cls):
        print "\n"
        if cls.minimax_vs_random_results != None:
            wins, losses, draws = cls.minimax_vs_random_results
            print "Minimax VS Random results:"
            print "  Wins: ", wins, "(", percentage(wins, PLAYS), "%)"
            print "  Losses: ", losses, "(", percentage(losses, PLAYS), "%)"
            print "  Draws: ", draws, "(", percentage(draws, PLAYS), "%)"
        if cls.random_vs_minimax_results != None:
            wins, losses, draws = cls.random_vs_minimax_results
            print "Random VS Minimax results:"
            print "  Wins: ", wins, "(", percentage(wins, PLAYS), "%)"
            print "  Losses: ", losses, "(", percentage(losses, PLAYS), "%)"
            print "  Draws: ", draws, "(", percentage(draws, PLAYS), "%)"

    # ------------------------------------------
    # Common tests
    # ------------------------------------------

    def versus(self, playerO, playerX, rounds):
        wins = 0
        losses = 0
        draws = 0
        for round in range(rounds):
            game = TicTacToe(playerO, playerX, False)
            while game.winner == None:
                game.update()
            if game.winner == O:
                wins += 1
            elif game.winner == X:
                losses += 1
            elif game.winner == DRAW:
                draws += 1
        return (wins, losses, draws)

    # ------------------------------------------
    # Minimax Vs Random
    # ------------------------------------------

    def test_minimax_vs_random(self):
        wins, losses, draws = self.versus(MINIMAX, RANDOM, PLAYS)
        self.__class__.minimax_vs_random_results = (wins, losses, draws)
        self.assertGreaterEqual(percentage(wins, PLAYS), 0.5)

    # ------------------------------------------
    # Random Vs Minimax
    # ------------------------------------------

    def test_random_vs_minimax(self):
        wins, losses, draws = self.versus(RANDOM, MINIMAX, PLAYS)
        self.__class__.random_vs_minimax_results = (wins, losses, draws)
        self.assertGreaterEqual(percentage(losses, PLAYS), 0.2)

if __name__ == '__main__':
    unittest.main()