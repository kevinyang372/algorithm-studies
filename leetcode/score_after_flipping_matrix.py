# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

 

# Example 1:

# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

# Note:

# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.

def matrixScore(self, A):
    if not A: return 0
    
    for i in range(len(A)):
        if A[i][0] == 0:
            for j in range(len(A[0])):
                A[i][j] = 1 - A[i][j]
    
    for j in range(1, len(A[0])):
        c = 0
        for i in range(len(A)):
            if A[i][j] == 0:
                c += 1
        if c > len(A) - c:
            for i in range(len(A)):
                A[i][j] = 1 - A[i][j]
                
    res = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            res += A[i][j] * 2 ** (len(A[0]) - 1 - j)
    
    return res
    