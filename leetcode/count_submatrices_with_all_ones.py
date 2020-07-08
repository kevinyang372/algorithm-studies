# Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

# Example 1:

# Input: mat = [[1,0,1],
#               [1,1,0],
#               [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:

# Input: mat = [[0,1,1,0],
#               [0,1,1,1],
#               [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# Example 3:

# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
# Example 4:

# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
 

# Constraints:

# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1

def numSubmat(self, mat: List[List[int]]) -> int:
        
    d = set()
    
    def check_size(m, n):
        for i in range(m, len(mat) + 1):
            for j in range(n, len(mat[0]) + 1):
                if mat[i - 1][j - 1] == 1:
                    if (m == 1 and n == 1) or (m == 1 and (i - m, j - n, i, j - 1) in d) or (n == 1 and (i - m, j - n, i - 1, j) in d) or ((i - m, j - n, i, j - 1) in d and (i - m, j - n, i - 1, j) in d):
                        d.add((i - m, j - n, i, j))
        
    for h in range(1, len(mat) + 1):
        for w in range(1, len(mat[0]) + 1):
            check_size(h, w)
    
    return len(d)