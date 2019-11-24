# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

# Example:

# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2 
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#              and 2 is the max number no larger than k (k = 2).
# Note:

# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

# brute force
def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
    d = {}
    max_val = -float('inf')
    
    def checkMax(a, b, c, e, max_val, k):
        if d[a, b, c, e] > max_val and d[a, b, c, e] <= k:
            return d[a, b, c, e]
        else:
            return max_val
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            d[i, j, i, j] = matrix[i][j]
            max_val = checkMax(i, j, i, j, max_val, k)
            if i == 0 and j == 0:
                continue
            elif i == 0:
                for dj in range(j):
                    d[0, dj, i, j] = d[0, dj, 0, j - 1] + matrix[i][j]
                    max_val = checkMax(0, dj, i, j, max_val, k)
            elif j == 0:
                for di in range(i):
                    d[di, 0, i, j] = d[di, 0, i - 1, 0] + matrix[i][j]
                    max_val = checkMax(di, 0, i, j, max_val, k)
            else:
                d[0, 0, i, j] = d[0, 0, i - 1, j - 1] + d[i, 0, i, j - 1] + d[0, j, i - 1, j] + matrix[i][j]
                max_val = checkMax(0, 0, i, j, max_val, k)
                for di in range(i + 1):
                    for dj in range(j + 1):
                        if (di != 0 or dj != 0):
                            if di > 0 and dj > 0:
                                d[di, dj, i, j] = d[0, 0, i, j] - d[0, 0, di - 1, j] - d[di, 0, i, dj - 1]
                            elif di > 0:
                                d[di, dj, i, j] = d[0, 0, i, j] - d[0, 0, di - 1, j]
                            else:
                                d[di, dj, i, j] = d[0, 0, i, j] - d[di, 0, i, dj - 1]
                                
                            max_val = checkMax(di, dj, i, j, max_val, k)
                            
    return max_val