"""
This is the tester file for TicTacToeBuilder

Author: Samuel Rodriguez
Date: 1/12/2021
"""
import unittest
from TicTacToeBuild import TicTacToeBuild

tc = unittest.TestCase()

def testprintBoard():
    """
    Checks that printBoard(board) works (need to check manually)
    """
    board = [[' ', 'X', ' '], ['O', 'X', 'O'], [' ', ' ', ' ']]
    tester = TicTacToeBuild(board = board)
    tester.printBoard()
    print()
    tester = TicTacToeBuild(n = 3)
    tester.printBoard()
    print()
    tester = TicTacToeBuild(n = 2)
    tester.printBoard()
    print()
    board = [[' ', 'O'], ['O', ' ']]
    tester = TicTacToeBuild(board = board)
    tester.printBoard()
    print()
    board = [[' ', ' ', ' ', 'X'], [' ', ' ', ' ', 'X'], [' ', ' ', ' ', 'X'], [' ', ' ', ' ', 'X']]
    tester = TicTacToeBuild(board = board)
    tester.printBoard()
    print()

def testMove():
    tester = TicTacToeBuild(3)
    # invalid piece to make a move with
    with tc.assertRaises(AssertionError):
        tester.move(0,0,'x')
    # invalid XorO type
    with tc.assertRaises(AssertionError):
        tester.move(0,0,0)
    # invalid row num
    with tc.assertRaises(AssertionError):
        tester.move(-1,0,'X')
    # invalid row type
    with tc.assertRaises(AssertionError):
        tester.move(True,0,'x')
    # invalid col num
    with tc.assertRaises(AssertionError):
        tester.move(0,100,'X')
    # invalid col type
    with tc.assertRaises(AssertionError):
        tester.move(0,'a','x')
    # valid first move
    tester.move(0,0, 'X')
    expected = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    tc.assertEqual(expected, tester.getBoard())
    # already filled position with same piece
    with tc.assertRaises(ValueError):
        tester.move(0,0,'X')
    # already filled position with different piece
    with tc.assertRaises(ValueError):
        tester.move(0,0,'O')
    # valid move to arbitrary row, first column
    tester = TicTacToeBuild(3)
    tester.move(1,0, 'O')
    expected = [[' ', ' ', ' '], ['O', ' ', ' '], [' ', ' ', ' ']]
    tc.assertEqual(expected, tester.getBoard())
    # valid move to arbitrary col, first row
    tester = TicTacToeBuild(3)
    tester.move(0,2, 'X')
    expected = [[' ', ' ', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    tc.assertEqual(expected, tester.getBoard())
    # valid move to arbitrary row and col
    tester = TicTacToeBuild(3)
    tester.move(1,1, 'O')
    expected = [[' ', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    tc.assertEqual(expected, tester.getBoard())
    # Arbitrary Number of valid moves
    tester = TicTacToeBuild(3)
    tester.move(1,0, 'O')
    expected = [[' ', ' ', ' '], ['O', ' ', ' '], [' ', ' ', ' ']]
    tc.assertEqual(expected, tester.getBoard())
    tester.move(2,1, 'X')
    expected = [[' ', ' ', ' '], ['O', ' ', ' '], [' ', 'X', ' ']]
    tc.assertEqual(expected, tester.getBoard())

def testGameOver():
    # invalid win row-wise (incomplete row)
    tester = TicTacToeBuild(3)
    tester.move(0,0,'X')
    tester.move(0,1,'X')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    #invalid win row-wise (row filled, but no win)
    tester.move(0,2,'O')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win col-wise (incomplete col)
    tester = TicTacToeBuild(3)
    tester.move(0,2, 'O')
    tester.move(1,2,'O')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win col-wise (col filled, but no win)
    tester.move(2,2,'X')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win left-diag-wise (incomplete)
    tester = TicTacToeBuild(3)
    tester.move(0,0, 'O')
    tester.move(1,1,'O')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win left-diag-wise (left-diag filled, but no win)
    tester.move(2,2,'X')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win right-diag-wise (incomplete)
    tester = TicTacToeBuild(3)
    tester.move(0,2, 'O')
    tester.move(1,1,'O')
    expected = False
    tc.assertEqual(expected, tester.gameOver())
    # invalid win right-diag-wise (right-diag filled, but no win)
    tester.move(2,0,'X')
    expected = False
    tc.assertEqual(expected, tester.gameOver())

    # valid win row wise
    tester = TicTacToeBuild(3)
    tester.move(1,0,"X")
    tester.move(1,1,"X")
    tester.move(1,2,"X")
    expected = True
    tc.assertEqual(expected, tester.gameOver())
    # valid win col wise
    tester = TicTacToeBuild(3)
    tester.move(0,1,"O")
    tester.move(1,1,"O")
    tester.move(2,1,"O")
    expected = True
    tc.assertEqual(expected, tester.gameOver())
    # valid win left diag wise
    tester = TicTacToeBuild(3)
    tester.move(0,0,"X")
    tester.move(1,1,"X")
    tester.move(2,2,"X")
    expected = True
    tc.assertEqual(expected, tester.gameOver())
    # valid win right diag wise
    tester = TicTacToeBuild(3)
    tester.move(0,2,"O")
    tester.move(1,1,"O")
    tester.move(2,0,"O")
    expected = True
    tc.assertEqual(expected, tester.gameOver())


#testprintBoard() - already tested
testMove()
testGameOver()
print("All tests passed successfully")
