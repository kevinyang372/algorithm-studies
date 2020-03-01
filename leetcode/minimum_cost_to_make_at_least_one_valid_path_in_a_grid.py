# Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

# You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

# Return the minimum cost to make the grid have at least one valid path.

 

# Example 1:


# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
# Example 2:


# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
# Example 3:


# Input: grid = [[1,2],[4,3]]
# Output: 1
# Example 4:

# Input: grid = [[2,2,2],[2,2,2]]
# Output: 3
# Example 5:

# Input: grid = [[4]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100

def minCost(self, grid: List[List[int]]) -> int:
        
    direction = {
        1: (0, 1),
        2: (0, -1),
        3: (1, 0),
        4: (-1, 0)
    }
    
    dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    queue = collections.deque([(0, 0, 0)])
    
    while queue:
        x, y, cost = queue.popleft()
        dx, dy = direction[grid[x][y]]
        dp[x][y] = min(dp[x][y], cost)
        
        if (x, y) == (len(grid) - 1, len(grid[0]) - 1): return cost
        
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and cost < dp[x + dx][y + dy]:
            queue.appendleft((x + dx, y + dy, cost))
        
        for ddx, ddy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if 0 <= x + ddx < len(grid) and 0 <= y + ddy < len(grid[0]) and (ddx, ddy) != (dx, dy) and cost + 1 < dp[x + ddx][y + ddy]:
                queue.append((x + ddx, y + ddy, cost + 1))
                
    return dp