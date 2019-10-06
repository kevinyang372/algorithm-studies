# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
 

# Note:

# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


# dp approach TLE
def updateMatrix(self, matrix):
        
    s = [[float('inf')] * len(matrix[0]) for _ in matrix]
    
    def search(x, y, direction):
        if matrix[x][y] == 0: s[x][y] = 0
        min_d = [s[x][y]]
        if direction == 'ul':
            if x > 0:
                min_d.append(1 + search(x - 1, y, direction))
            if y > 0:
                min_d.append(1 + search(x, y - 1, direction))
        else:
            if x < len(matrix) - 1:
                min_d.append(1 + search(x + 1, y, direction))
            if y < len(matrix[0]) - 1:
                min_d.append(1 + search(x, y + 1, direction))

        res = min(min_d)
        s[x][y] = res
        return res
    
    search(0, 0, 'dr')
    search(len(matrix) - 1, len(matrix[0]) - 1, 'ul')
    
    return s