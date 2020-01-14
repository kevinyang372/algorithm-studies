# Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100

# TLE
def matrixBlockSum(self, mat, K):
    res = [[0] * len(mat[0]) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i][j] = sum([mat[i - di][j - dj] for di in range(-K, K + 1) for dj in range(-K, K + 1) if 0 <= i - di < len(mat) and 0 <= j - dj < len(mat[0])])
            
    return res

# dp
def matrixBlockSum(self, mat, K):
    col, row = collections.defaultdict(dict), collections.defaultdict(dict)
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == 0:
                row[i][j] = mat[i][j]
            else:
                row[i][j] = row[i][j - 1] + mat[i][j]
                
            if i == 0:
                col[i][j] = mat[i][j]
            else:
                col[i][j] = col[i - 1][j] + mat[i][j]
    
    res = [[0] * len(mat[0]) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0 and j == 0:
                res[i][j] = sum([row[temp][min(K, len(mat[0]) - 1)] for temp in range(K + 1) if temp in row])
            elif j == 0:
                res[i][j] = res[i - 1][j]
                if i + K < len(mat):
                    res[i][j] += row[i + K][min(K, len(mat[0]) - 1)]
                if i - K > 0:
                    res[i][j] -= row[i - K - 1][min(K, len(mat[0]) - 1)]
            else:
                res[i][j] = res[i][j - 1]
                if j + K < len(mat[0]):
                    if i - K <= 0:
                        res[i][j] += col[min(i + K, len(mat) - 1)][j + K]
                    else:
                        res[i][j] += col[min(i + K, len(mat) - 1)][j + K] - col[i - K - 1][j + K]
                if j - K > 0:
                    if i - K <= 0:
                        res[i][j] -= col[min(i + K, len(mat) - 1)][j - K - 1]
                    else:
                        res[i][j] -= col[min(i + K, len(mat) - 1)][j - K - 1] - col[i - K - 1][j - K - 1]
                                
    return res