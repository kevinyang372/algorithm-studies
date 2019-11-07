# A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".

# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.

# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false

# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# Note:

# board is a length-3 array of strings, where each string board[i] has length 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.

def validTicTacToe(self, board):
    count_0 = count_1 = 0
    row = collections.Counter()
    col = collections.Counter()
    diagonal = collections.Counter()
    winning_satisfied = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                count_0 += 1
                row[i] -= 1
                if row[i] == -3:
                    if winning_satisfied > 0:
                        return False
                    else:
                        winning_satisfied -= 1
                
                col[j] -= 1
                if col[j] == -3:
                    if winning_satisfied > 0:
                        return False
                    else:
                        winning_satisfied -= 1
                
                if i == j:
                    diagonal[1] -= 1
                    if diagonal[1] == -3:
                        if winning_satisfied > 0:
                            return False
                        else:
                            winning_satisfied -= 1
                if i == 2 - j:
                    diagonal[-1] -= 1
                    if diagonal[-1] == -3:
                        if winning_satisfied > 0:
                            return False
                        else:
                            winning_satisfied -= 1
            elif board[i][j] == 'X':
                count_1 += 1
                row[i] += 1
                if row[i] == 3:
                    if winning_satisfied < 0:
                        return False
                    else:
                        winning_satisfied += 1
                
                col[j] += 1
                if col[j] == 3:
                    if winning_satisfied < 0:
                        return False
                    else:
                        winning_satisfied += 1
                
                if i == j:
                    diagonal[1] += 1
                    if diagonal[1] == 3:
                        if winning_satisfied < 0:
                            return False
                        else:
                            winning_satisfied += 1
                if i == 2 - j:
                    diagonal[-1] += 1
                    if diagonal[-1] == 3:
                        if winning_satisfied < 0:
                            return False
                        else:
                            winning_satisfied += 1
    
    if count_0 > count_1 or count_1 - count_0 > 1:
        return False
    elif count_0 == count_1 and winning_satisfied > 0:
        return False
    elif count_0 < count_1 and winning_satisfied < 0:
        return False
    return True