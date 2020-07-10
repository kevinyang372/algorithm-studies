# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

# Return the maximum number of cherries collection using both robots  by following the rules below:

# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.
 

# Example 1:



# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
# Example 2:



# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
# Example 3:

# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
# Example 4:

# Input: grid = [[1,1],[1,1]]
# Output: 4
 

# Constraints:

# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 

# TLE
def cherryPickup(self, grid: List[List[int]]) -> int:
        
    @lru_cache
    def search(i, r1_j, r2_j):
        if r1_j == r2_j:
            curr = grid[i][r1_j]
        else:
            curr = grid[i][r1_j] + grid[i][r2_j]
            
        if i == len(grid) - 1: return curr
        
        max_val = -float('inf')
        for dj_1 in [1, -1, 0]:
            new_j1 = r1_j + dj_1
            if 0 <= new_j1 < len(grid[0]):
                for dj_2 in [1, -1, 0]:
                    new_j2 = r2_j + dj_2
                    if 0 <= new_j2 < len(grid[0]):
                        max_val = max(max_val, search(i + 1, new_j1, new_j2))
        return curr + max_val
    
    return search(0, 0, len(grid[0]) - 1)

# bottom up
def cherryPickup(self, grid: List[List[int]]) -> int:
        
    dp = [[[0] * len(grid[0]) for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for i in range(len(grid) - 1, -1, -1):
        for j1 in range(0, len(grid[0])):
            for j2 in range(0, len(grid[0])):
                if j1 == j2:
                    curr = grid[i][j1]
                else:
                    curr = grid[i][j1] + grid[i][j2]
                    
                if i == len(grid) - 1:
                    dp[i][j1][j2] = curr
                else:
                    dp[i][j1][j2] = curr + max(dp[i + 1][j1 + dj1][j2 + dj2] for dj1 in [0, 1, -1] for dj2 in [0, 1, -1] if 0 <= j1 + dj1 < len(grid[0]) and 0 <= j2 + dj2 < len(grid[0]))
    
    return dp[0][0][-1]