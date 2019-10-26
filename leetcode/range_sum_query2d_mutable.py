# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class BIT:
    
    def __init__(self, arr):
        self.bit = [0] * (len(arr) + 1)
        self.construct(arr)
        
    def sums(self, index):
        index += 1
        s = 0
        
        while index > 0:
            s += self.bit[index]
            index -= index & -index
        
        return s
    
    def update(self, index, value):
        index += 1
        
        while index < len(self.bit):
            self.bit[index] += value
            index += index & -index
        
    def construct(self, arr):
        for i, v in enumerate(arr):
            self.update(i, v)

class NumMatrix(object):

    def __init__(self, matrix):
        self.bits = []
        self.mat = matrix
        for v in matrix:
            self.bits.append(BIT(v))
        

    def update(self, row, col, val):
        delta = val - self.mat[row][col]
        self.mat[row][col] = val
        self.bits[row].update(col, delta)
        

    def sumRegion(self, row1, col1, row2, col2):
        s = 0
        for i in range(row1, row2 + 1):
            s += self.bits[i].sums(col2) - self.bits[i].sums(col1 - 1)
        return s