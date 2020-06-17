# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


def solve(self, board):

    if not board: return
        
    mat = [[0] * len(board[0]) for _ in board]
    
    self.mat = mat
    self.board = board

    for i in range(len(self.board)):
        if self.board[i][0] == 'O':
            self.mat[i][0] = 1
            self.find_branches([i, 0])
        if self.board[i][-1] == 'O':
            self.mat[i][-1] = 1
            self.find_branches([i, len(self.board[0]) - 1])
            
    for t in range(len(self.board[0])):
        if self.board[0][t] == 'O':
            self.mat[0][t] = 1
            self.find_branches([0, t])
        if self.board[-1][t] == 'O':
            self.mat[-1][t] = 1
            self.find_branches([len(self.board) - 1, t])

    for m in range(len(board)):
        for n in range(len(board[0])):
            if mat[m][n] == 0:
                board[m][n] = 'X'

def find_branches(self, current):
    
    if self.inbound([current[0] - 1, current[1]]) and self.board[current[0] - 1][current[1]] == 'O' and self.mat[current[0] - 1][current[1]] == 0:
        self.mat[current[0] - 1][current[1]] = 1
        self.find_branches([current[0] - 1, current[1]])
    if self.inbound([current[0] + 1, current[1]]) and self.board[current[0] + 1][current[1]] == 'O' and self.mat[current[0] + 1][current[1]] == 0:
        self.mat[current[0] + 1][current[1]] = 1
        self.find_branches([current[0] + 1, current[1]])
    if self.inbound([current[0], current[1] - 1]) and self.board[current[0]][current[1] - 1] == 'O' and self.mat[current[0]][current[1] - 1] == 0:
        self.mat[current[0]][current[1] - 1] = 1
        self.find_branches([current[0], current[1] - 1])
    if self.inbound([current[0], current[1] + 1]) and self.board[current[0]][current[1] + 1] == 'O' and self.mat[current[0]][current[1] + 1] == 0:
        self.mat[current[0]][current[1] + 1] = 1
        self.find_branches([current[0], current[1] + 1])
    
def inbound(self, current):
    
    if current[0] < 0 or current[0] >= len(self.board) or current[1] < 0 or current[1] >= len(self.board[0]):
        return False
    
    return True


# TLE
def solve(self, board: List[List[str]]) -> None:
        
    visited = set()
    
    def search(i, j):
        if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
            on_border = True
        else:
            on_border = False
            
        visited.add((i, j))
        connected = [(i, j)]
        
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and board[i + di][j + dj] == 'O' and (i + di, j + dj) not in visited:
                temp, lis = search(i + di, j + dj)
                on_border = on_border or temp
                connected += lis
        
        return on_border, connected
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O' and (i, j) not in visited:
                border, connected = search(i, j)
                if not border:
                    for ii, jj in connected:
                        board[ii][jj] = 'X'
                        
    return board