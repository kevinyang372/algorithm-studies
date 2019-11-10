# Write a program that takes as arugments a 2D array and a 1D array, and checks whether the 1D array occurs in the 2D array.

def searchSequence(grid, arr):
    dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and arr[dp[i + di][j + dj] + 1] == grid[i][j]:
                    dp[i][j] = max(dp[i + di][j + dj] + 1, dp[i][j])
                    
            if dp[i][j] == len(arr) - 1:
                return True
    return False