# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.

# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.

def numDistinctIslands(self, grid):
        
    visited = set()
    
    def dfs(x, y):
        res = [[0, 0, 0, 0]]
        for i, (dx, dy) in enumerate([[0, 1], [1, 0], [-1, 0], [0, -1]]):
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
                visited.add((x + dx, y + dy))
                res[0][i] = 1
                res += dfs(x + dx, y + dy)
                
        return res
    
    fin = set()
    for p in range(len(grid)):
        for q in range(len(grid[0])):
            if grid[p][q] == 1 and (p, q) not in visited:
                visited.add((p, q))
                fin.add(tuple([tuple(i) for i in dfs(p, q)]))
    
    return len(fin)