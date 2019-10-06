# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# Input:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]

# Output:

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

def multiplication(A, B):
    row_A, col_A = len(A), len(A[0])
    row_B, col_B = len(B), len(B[0])
    
    res = [[0] * col_B for _ in range(row_A)]
    
    def dotProduct(i, j):
        sums = 0
        for index in range(col_A):
            sums += A[i][index] * B[index][j]
        return sums
    
    for t1 in range(row_A):
        for t2 in range(col_B):
            res[t1][t2] = dotProduct(t1, t2)
            
    return res