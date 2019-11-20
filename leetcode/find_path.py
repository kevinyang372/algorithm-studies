# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

# Example 1:

# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:

# Example 2:

# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:

 

# Note:

# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].

# dp
def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    res = 0
    
    for _ in range(N):
        temp = [[0] * n for _ in range(m)]
        for t in range(m):
            for k in range(n):
                if dp[t][k] > 0:
                    for dt, dk in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        if 0 <= t + dt < m and 0 <= k + dk < n:
                            temp[t + dt][k + dk] += dp[t][k]
                        else:
                            res += dp[t][k]
        dp = temp
        
    return res % (10**9 + 7)