# You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

# Notice that the modulo is performed after getting the maximum product.

 

# Example 1:

# Input: grid = [[-1,-2,-3],
#                [-2,-3,-3],
#                [-3,-3,-2]]
# Output: -1
# Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:

# Input: grid = [[1,-2,1],
#                [1,-2,1],
#                [3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:

# Input: grid = [[1, 3],
#                [0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
# Example 4:

# Input: grid = [[ 1, 4,4,0],
#                [-2, 0,0,1],
#                [ 1,-1,1,1]]
# Output: 2
# Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
 

# Constraints:

# 1 <= rows, cols <= 15
# -4 <= grid[i][j] <= 4

def maxProductPath(self, grid: List[List[int]]) -> int:
    dp = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    temp = 1
    for i in range(len(grid)):
        temp *= grid[i][0]
        dp[i][0] = [temp, temp]
    
    temp = 1
    for j in range(len(grid[0])):
        temp *= grid[0][j]
        dp[0][j] = [temp, temp]
    
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            
            top = dp[i - 1][j]
            left = dp[i][j - 1]
            
            if grid[i][j] > 0:
                dp[i][j][0] = max(top[0] * grid[i][j], left[0] * grid[i][j])
                dp[i][j][1] = min(top[1] * grid[i][j], left[1] * grid[i][j])
            else:
                dp[i][j][0] = max(top[1] * grid[i][j], left[1] * grid[i][j])
                dp[i][j][1] = min(top[0] * grid[i][j], left[0] * grid[i][j])
    
    return dp[-1][-1][0] % (10 ** 9 + 7) if dp[-1][-1][0] >= 0 else -1