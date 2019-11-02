# Design a Tic-tac-toe game that is played between two players on a n x n grid.

# You may assume the following rules:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

# TicTacToe toe = new TicTacToe(3);

# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?

class TicTacToe(object):

    def __init__(self, n):
        self.board = [[None] * n for _ in range(n)]
        
    def checkRow(self, value, row):
        return all([i == value for i in self.board[row]])
    
    def checkCol(self, value, col):
        return all([self.board[i][col] == value for i in range(len(self.board))])
    
    def checkDiagonal(self, value, row, col):
        if row != col and row + col != len(self.board) - 1: return False
        l = len(self.board)
        return all([self.board[i][i] == value for i in range(l)]) or all([self.board[i][l - i - 1] == value for i in range(l)])
        
    def move(self, row, col, player):
        self.board[row][col] = player
        res = self.checkRow(player, row) or self.checkCol(player, col) or self.checkDiagonal(player, row, col)
        
        if not res:
            return 0
        else:
            return player