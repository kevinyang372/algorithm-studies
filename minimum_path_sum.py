# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):

    if not grid:
        return 0

    curr = grid[0][0]
    result = []

    if len(grid) > 1:
        result.append(curr + minPathSum(grid[1:]))

    if len(grid[0]) > 1:
        result.append(curr + minPathSum([t[1:] for t in grid]))

    return min(result) if result else curr


# dp
def minPathSum(grid):

    m,n = (len(grid), len(grid[0]))
    mem = [[0] * n] * m
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                mem[i][j] = grid[i][j]
            elif i == m-1:
                mem[i][j] = grid[i][j] + mem[i][j+1]
            elif j == n-1:
                mem[i][j] = grid[i][j] + mem[i+1][j]
            else:
                mem[i][j] = grid[i][j] + min(mem[i+1][j], mem[i][j+1])
    return mem[0][0]