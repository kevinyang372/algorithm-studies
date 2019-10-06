# On a 2-dimensional grid, there are 4 types of squares:

# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

# Example 1:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:

# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
 

# Note:

# 1 <= grid.length * grid[0].length <= 20

def uniquePathsIII(self, grid):
        
    if not grid: return 0
    
    start = end = (-1, -1)
    count = 0
    
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == 1:
                start = (m, n)
            elif grid[m][n] == 2:
                end = (m, n)
            elif grid[m][n] == 0:
                count += 1
    
    if start[0] < 0 or end[0] < 0: return 0
    
    def dfs(node, c):
        
        x, y = node
        res = 0
        
        if node == end:
            if c == 0: 
                return 1
            else: 
                return 0
            
        grid[x][y] = -1
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != -1:
                res += dfs((x + dx, y + dy), c - 1)
                
        grid[x][y] = 0
        return res
    
    return dfs(start, count + 1)