# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

# Note:

# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.

class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.solve()
        print(self.board)

    def find_unsolved(self):

        for m in range(9):
            for n in range(9):
                if self.board[m][n] == '.':
                    return m, n

        return -1, -1

    def solve(self):

        row, col = self.find_unsolved()
        if row == col == -1:
            return True

        for num in range(1, 10):
            if self.valid(row, col, str(num)):
                self.board[row][col] = str(num)
                if self.solve():
                    return True
                self.board[row][col] = '.'

        return False

    def valid(self, row, col, val):

        for i in self.board[row]:
            if i == val:
                return False

        for i in self.board:
            if i[col] == val:
                print(i[col], val)
                return False

        parent_row = row - row%3
        parent_col = col - col%3

        for m in range(parent_row, parent_row + 3):
            for n in range(parent_col, parent_col + 3):
                if self.board[m][n] == val:
                    return False

        return True