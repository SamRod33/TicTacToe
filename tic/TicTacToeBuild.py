"""
This is a console text game of tic tac toe

In this file contains all of the methods used to build and maintain
the tic tac toe game

Author: Samuel Rodriguez
Date: 1/12/2021
"""
from Consts import *

class TicTacToeBuild:

    # ATTRIBUTES
    # _board   : n x n 2D array of entries on the board
    # _size    : int representing num of row/col (basically n)
    # _currTile: the tile currently highlighted for choosing

    def buildEmptyBoard(self, n):
        """
        Returns n x n blank board

        Parameter n: the number of rows and columns of game board
        Precondition: n is a positive int
        """
        assert type(n) == int, "n must be of type int"
        assert n > 0, "n must be a positive int"
        output = []
        for row in range(n):
            temp = []
            for col in range(n):
                temp.append(" ")
            output.append(temp)

        return output

    def __init__(self, n = -1, board = None):
        self._board = self.buildEmptyBoard(n) if board is None else board
        self._size = len(self._board)
        self._currTile = {'i': 0, 'j': 0}

    def printBoard(self):
        """
        Prints the tic tac board

        The board's structure is a 2D list such that each nested list is a
        row on the tic tac toe board.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Example: [[' ', 'X', ' '], ['O', 'X', 'O'], [' ', ' ', ' ']]
        Is printed as:
           | X |
        -----------
         O | X | O
        -----------
           |   |

        Parameter board: the tic tac toe board to print
        Precondition: board is a 2D list
        """
        assert type(self._board) == list, "board is not a list"
        for alist in self._board:
            assert type(alist) == list, "board list does not contain lists"

        for row in range(self._size):
            for col in range(len(self._board[row])):
                if col < len(self._board[row])-1:
                    print(" %s |" % self._board[row][col], end="")
                else:
                    print(" %s" % self._board[row][col], end="")
            print()
            if row < len(self._board) -1:
                print("-" * (len(self._board[row]) * 4 - 1))

    def move(self, row, col, XorO):
        """
        Updates the board at position (row, col) with either an X or O
        This function raises a ValueError if this position is already filled

        Parameter row: row position to update
        Precondition: row is a valid row and an int

        Parameter col: col position to update
        Precondition: col is a valid col and an int

        Parameter XorO: the piece to replace an empty position on the board
        Precondition: XorO is a string that is 'X' or 'O' ONLY
        """
        assert type(row) == int, "row must be an int"
        assert -1 < row < self._size, "row is not a valid row num"
        assert type(col) == int, "col must be an int"
        assert -1 < col < self._size, "col is not a valid col num"
        assert type(XorO) == str, "XorO must be a string"
        assert XorO == "X" or XorO == "O", "XorO must be 'X' or 'O'"

        if self._board[row][col] == "X" or self._board[row][col] == "O":
            raise ValueError("Board position (%d, %d) is already filled.", (row, col))

        self._board[row][col] = XorO

    def gameOver(self):
        """
        Returns True if there is a winner, false otherwise

        A player wins when their moves connect to form a straight line
        across the entire board (vertically, horizontally, or diagonally)

        Examples:
        (2nd column win)   (1st row win)   (diagonal win)
           | X |            O | O | O       X | X |
        -----------        -----------     -----------
         O | X | O          O | X | O       O | X | O
        -----------        -----------     -----------
           | X |              | X |           |   | X

        THESE DOES NOT WORK:
        (O instead of X)  (incomplete)    (Not proper diagonal)
           | O |              | O | O         |   |
        -----------        -----------     -----------
         O | X | O            |   | O       X |   |
        -----------        -----------     -----------
           | X |              |   |           | X |
        """

        def checkRow(XorO, row):
            """
            Returns False if at least one column in the row does not
            contain all X's or O's, True Otherwise

            Parameter XorO: whether we check for X's or O's
            Precondition: XorO is a string with "X" or "O" ONLY

            Parameter row: row to check
            Precondition: row is a valid row and an int
            """
            assert type(XorO) == str, "XorO must be a string"
            assert XorO == "X" or XorO == "O", "XorO must be 'X' or 'O'"
            assert type(row) == int, "row must be an int"
            assert -1 < row < self._size, "row is not a valid row num"
            for col in range(self._size):
                if self._board[row][col] != XorO:
                    return False
            return True

        def checkCol(XorO, col):
            """
            Returns False if at least one row in the column does not
            contain all X's or O's, True Otherwise

            Parameter XorO: whether we check for X's or O's
            Precondition: XorO is a string with "X" or "O" ONLY

            Parameter col: column to check
            Precondition: col is a valid column and an int
            """
            assert type(XorO) == str, "XorO must be a string"
            assert XorO == "X" or XorO == "O", "XorO must be 'X' or 'O'"
            assert type(col) == int, "col must be an int"
            assert -1 < col < self._size, "col is not a valid col num"
            for row in range(self._size):
                if self._board[row][col] != XorO:
                    return False
            return True

        def checkDiag(XorO, isLeft= True):
            """
            Returns False if at least one entry along the diagonal does not
            contain all X's or O's, True Otherwise

            Parameter XorO: whether we check for X's or O's
            Precondition: XorO is a string with "X" or "O" ONLY

            Parameter isLeft: choose whether to do left or right diagonal
            Precondition: isLeft is a bool
            """
            assert type(XorO) == str, "XorO must be a string"
            assert XorO == "X" or XorO == "O", "XorO must be 'X' or 'O'"
            assert type(isLeft) == bool, "isLeft must be a bool"
            if isLeft:
                for h in range(1,self._size):
                    if self._board[h][h] != XorO:
                        return False
            else:
                for h in range(1, self._size):
                    if self._board[h][(self._size - 1) - h] != XorO:
                        return False
            return True

        # check left diagonal
        XorO = self._board[0][0]
        if (XorO == 'X' or XorO == 'O') and checkDiag(XorO, isLeft=True):
            return True

        # check right diagonal
        XorO = self._board[0][-1]
        if (XorO == 'X' or XorO == 'O') and checkDiag(XorO, isLeft=False):
            return True

        # check each row
        for i in range(self._size):
            XorO = self._board[i][0]
            if (XorO == 'X' or XorO == 'O') and checkRow(XorO, i):
                return True

        # check each col
        for j in range(self._size):
            XorO = self._board[0][j]
            if (XorO == 'X' or XorO == 'O') and checkCol(XorO, j):
                return True

        return False

    def tie(self):
        """
        Returns True if the board is filled, meaning a tie has occurred
        False otherwise
        """
        for row in self._board:
            for col in row:
                if col == ' ':
                    return False
        return True

    def insertMark(self, direction):
        """
        Returns current position of player cursor

        Modifies board such that current selection from player is marked with
        '*' on the board tile based on the direction to move

        If the bounds of the direction are exceeded, loop around to the start

        Parameter direction: the direction to move on the board
        Precondition: direction is LEFT, RIGHT, UP, or DOWN

        Parameter start: if game just started, place marker at (0,0)
        Precondition: start is a bool
        """
        assert direction == LEFT or direction == RIGHT or direction == UP or \
            direction == DOWN, "Not a valid direction to move"
        if direction == LEFT:
            j, i = self.searchForEmpty(False, False)
            self._currTile['j'] = j
            self._currTile['i'] = i
        if direction == RIGHT:
            j, i = self.searchForEmpty(False, True)
            self._currTile['j'] = j
            self._currTile['i'] = i
        if direction == UP:
            i, j = self.searchForEmpty(True, False)
            self._currTile['i'] = i
            self._currTile['j'] = j
        if direction == DOWN:
            i, j = self.searchForEmpty(True, True)
            self._currTile['i'] = i
            self._currTile['j'] = j

        i = self._currTile['i']
        j = self._currTile['j']
        self._board[i][j] = '*'
        return self._currTile.values()

    def startMark(self):
        """
         Returns current position of player cursor

         Scans board until it finds nonempty spot or no spots left
        """
        for i in range(self._size):
            for j in range(self._size):
                if not self.isFilled(i, j):
                    self._currTile['i'] = i
                    self._currTile['j'] = j
                    self._board[i][j] = '*'
                    return self._currTile.values()

    def removeMark(self):
        """
        Removes mark on board at the tile positioned at _currTile
        """
        i = self._currTile['i']
        j = self._currTile['j']
        self._board[i][j] = ' '

    def isFilled(self, row, col):
        """
        Returns True if this tile (row, col) is filled with X or O
        False Otherwise
        """
        return self._board[row][col] == 'X' or self._board[row][col] == 'O'

    def searchForEmpty(self, is_i, is_right_down):
        """
        Returns k, h such that (k, h) or (h, k) contains an empty tile

        Parameter is_i: If we iterate over row or not
        Precondition: is_i is a bool

        Parameter is_right_down: If we search right/down or left/up
        Precondition: is_right is either 1 or -1
        """
        assert type(is_i) == bool, "is_i is not of type bool"
        assert type(is_right_down) == bool, "is_right_down is not of type bool"
        k_axis = 'j'
        h_axis = 'i'
        dir = BACK
        if is_right_down:
            dir = FORWARD
        if is_i:
            k_axis = 'i'
            h_axis = 'j'
        k = self._currTile[k_axis] + dir
        h = self._currTile[h_axis]
        if k < 0:
            k = self._size - 1
        if k > self._size - 1:
            k = 0
        if is_i:
            while self.isFilled(k, self._currTile['j']):
                k += dir
                # loop back to start
                if k < 0:
                    k = self._size - 1
                if k > self._size - 1:
                    k = 0
            if k == self._currTile['i']:
                k, h = self.findEmpty()
        else:
            while self.isFilled(self._currTile['i'], k):
                k += dir
                # loop back to start
                if k < 0:
                    k = self._size - 1
                if k > self._size - 1:
                    k = 0
            if k == self._currTile['j']:
                h, k = self.findEmpty()
        return k, h

    def findEmpty(self):
        """
        Returns i, j such that this tile is not filled
        Performs linear search (should improve later)
        """
        self.printBoard()
        for i in range(self._size):
            for j in range(self._size):
                if not self.isFilled(i, j) and i != self._currTile['i'] \
                        and j != self._currTile['j']:
                    return i, j
        # all tiles filled
        return -2, -2

    # GETTERS AND SETTERS
    def getBoard(self):
        """
        Returns the board
        """
        return self._board

    def getSize(self):
        """
        Returns size of the board
        """
        return self._size
