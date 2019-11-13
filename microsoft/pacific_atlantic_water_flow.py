# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:

# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
 

# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

def pacificAtlantic(self, matrix):
        
    if not matrix: return
    
    pacific = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    atlantic = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    
    fr_p = [[0, i] for i in range(len(matrix[0]))] + [[i, 0] for i in range(len(matrix))]
    
    fr_a = [[len(matrix) - 1, i] for i in range(len(matrix[0]))] + [[i, len(matrix[0]) - 1] for i in range(len(matrix))]
    
    
    for x, y in fr_p:
        pacific[x][y] = True
        
    for x, y in fr_a:
        atlantic[x][y] = True
    
    def dfs(maps, frontier):
        while frontier:
            x, y = frontier.pop()
            
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= x + dx < len(maps) and 0 <= y + dy < len(maps[0]) and not maps[x + dx][y + dy] and matrix[x + dx][y + dy] >= matrix[x][y]:
                    maps[x + dx][y + dy] = True
                    frontier.append([x + dx, y + dy])
                    
        return maps
    
    pacific = dfs(pacific, fr_p)
    atlantic = dfs(atlantic, fr_a)
    
    return [[x, y] for x in range(len(matrix)) for y in range(len(matrix[0])) if pacific[x][y] and atlantic[x][y]]