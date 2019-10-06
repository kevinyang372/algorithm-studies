# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?



# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# brute force - TLE
def uniquePathsWithObstacles(self, obstacleGrid):
        
    if not obstacleGrid or obstacleGrid[-1][-1] == 1: return 0
    
    stack = [[0, 0]]
    count = 0
    l1, l2 = len(obstacleGrid), len(obstacleGrid[0])
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) == (l1 - 1, l2 - 1):
                    count += 1
        
        for dx, dy in [(1, 0), (0, 1)]:
            if 0 <= x + dx < l1 and 0 <= y + dy < l2 and obstacleGrid[x][y] != 1:
                stack.append([x + dx, y + dy])
        
    return count

# dp
def uniquePathsWithObstacles(self, obstacleGrid):
        
    if not obstacleGrid or obstacleGrid[-1][-1] == 1: return 0
    
    res = [[0] * len(obstacleGrid[0]) for _ in obstacleGrid]
    
    for t in range(len(obstacleGrid[0])):
        if obstacleGrid[0][t] == 0:
            res[0][t] = 1
        else:
            break
    
    for t in range(len(obstacleGrid)):
        if obstacleGrid[t][0] == 0:
            res[t][0] = 1
        else:
            break
    
    for m in range(1, len(obstacleGrid)):
        for n in range(1, len(obstacleGrid[0])):
            if obstacleGrid[m][n] == 1:
                continue
            else:
                res[m][n] = res[m - 1][n] + res[m][n - 1]
                
    return res[-1][-1]