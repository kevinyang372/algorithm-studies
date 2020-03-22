# Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.


# You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

# Notice that you are not allowed to change any street.

# Return true if there is a valid path in the grid or false otherwise.

 

# Example 1:


# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
# Example 2:


# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
# Example 3:

# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
# Example 4:

# Input: grid = [[1,1,1,1,1,1,3]]
# Output: true
# Example 5:

# Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
# Output: true
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6

def hasValidPath(self, grid: List[List[int]]) -> bool:
        
    d = {
        1: ('l', 'r'),
        2: ('u', 'd'),
        3: ('l', 'd'),
        4: ('r', 'd'),
        5: ('l', 'u'),
        6: ('r', 'u')
    }
    
    def traverse(node, start):
        if node == (len(grid) - 1, len(grid[0]) - 1): return True
        x, y = node
        
        d1, d2 = d[grid[x][y]]
        if d1 == start:
            next = d2
        else:
            next = d1
            
        if next == 'l':
            dx, dy = 0, -1
            rep = 'r'
        elif next == 'r':
            dx, dy = 0, 1
            rep = 'l'
        elif next == 'u':
            dx, dy = -1, 0
            rep = 'd'
        else:
            dx, dy = 1, 0
            rep = 'u'
        
        
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and rep in d[grid[x + dx][y + dy]]:
            return traverse((x + dx, y + dy), rep)
        return False
    
    return traverse((0, 0), d[grid[0][0]][0]) or traverse((0, 0), d[grid[0][0]][1])