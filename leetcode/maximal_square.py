# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

def maximalSquare(matrix):

    if not matrix: return 0

    res = [[0] * len(i) for i in matrix]
    count = 0

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if m == 0 or n == 0:
                res[m][n] = 1 if matrix[m][n] == "1" else 0
            elif matrix[m][n] == "1":
                res[m][n] = min(res[m - 1][n - 1], res[m][n -1], res[m - 1][n]) + 1

            count = max(res[m][n], count)

    return count