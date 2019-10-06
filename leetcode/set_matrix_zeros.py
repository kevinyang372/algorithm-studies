# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# O(M + N) space O(MN) time
def setZeroes(self, matrix):
        
    if not matrix: return
    m, n = len(matrix), len(matrix[0])
    rows, columns = set(), set()
    
    for i in range(m):
        for t in range(n):
            if matrix[i][t] == 0:
                rows.add(i)
                columns.add(t)
                
    for i in range(m):
        for t in range(n):
            if i in rows or t in columns:
                matrix[i][t] = 0