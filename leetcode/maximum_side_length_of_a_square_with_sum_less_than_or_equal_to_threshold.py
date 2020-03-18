# Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
# Example 3:

# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
# Example 4:

# Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
# Output: 2
 

# Constraints:

# 1 <= m, n <= 300
# m == mat.length
# n == mat[i].length
# 0 <= mat[i][j] <= 10000
# 0 <= threshold <= 10^5

def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
    rows, cols = collections.defaultdict(dict), collections.defaultdict(dict)
    
    for i in range(len(mat)):
        rows[i][-1] = 0
        for row, val in enumerate(mat[i]):
            if i == 0: cols[row][-1] = 0
            rows[i][row] = rows[i][row - 1] + val
            cols[row][i] = cols[row][i - 1] + val
            
    max_val = 0
    for m in range(len(mat)):
        for n in range(len(mat[0])):
            
            sums = mat[m][n]
            x, y = m, n

            while sums <= threshold:
                max_val = max(max_val, x - m + 1)
                if x + 1 < len(mat) and y + 1 < len(mat[0]):
                    dx = rows[x + 1][y] - rows[x + 1][n - 1]
                    dy = cols[y + 1][x] - cols[y + 1][m - 1]
                    sums += mat[x + 1][y + 1] + dx + dy
                    
                    x += 1
                    y += 1
                else:
                    break
    
    return max_val