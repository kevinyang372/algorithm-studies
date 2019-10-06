# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

# O(N) solution (not in-place)
def gameOfLife(board):

    sudo_board = [[None] * len(board[0]) for _ in board]
    for i in range(len(board)):
        for t in range(len(board[0])):
            count = 0
            for (x, y) in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if i + x >= 0 and i + x < len(board) and t + y >= 0 and t + y < len(board[0]) and board[i + x][t + y] == 1:
                    count += 1

            if board[i][t] == 0:
                if count == 3:
                    sudo_board[i][t] = 1
                else:
                    sudo_board[i][t] = 0
            else:
                if count < 2 or count > 3:
                    sudo_board[i][t] = 0
                else:
                    sudo_board[i][t] = 1

    for i in range(len(board)):
        for t in range(len(board[0])):
            board[i][t] = sudo_board[i][t]

# O(N) time O(1) space solution (in-place)
def gameOfLife(board):

    for i in range(len(board)):
        for t in range(len(board[0])):
            count = 0
            for (x, y) in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if i + x >= 0 and i + x < len(board) and t + y >= 0 and t + y < len(board[0]) and abs(board[i + x][t + y]) == 1:
                    count += 1
                    
            if board[i][t] == 0:
                if count == 3: 
                    board[i][t] = 2
            else:
                if count < 2 or count > 3: 
                    board[i][t] = -1
    
    for m in range(len(board)):
        for n in range(len(board[0])):
            if board[m][n] == 2: board[m][n] = 1
            if board[m][n] == -1: board[m][n] = 0