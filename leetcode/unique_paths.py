# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Note: m and n will be at most 100.

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28

def uniquePaths(m: int, n: int) -> int:

    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for t in range(m - 1, -1, -1):
            if t == m - 1 or i == n - 1:
                matrix[i][t] = 1
            else:
                matrix[i][t] = matrix[i + 1][t] + matrix[i][t + 1]

    return matrix[0][0]