# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

# Example:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# Output:  [1,2,4,7,5,3,6,8,9]

# Explanation:

 

# Note:

# The total number of elements of the given matrix will not exceed 10,000.

def findDiagonalOrder(self, matrix):
    if not matrix: return []
    
    res = []
    pos, target = [0, 0], [len(matrix) - 1, len(matrix[0]) - 1]
    di = 'UP'
    
    while pos != target:
        res.append(matrix[pos[0]][pos[1]])
        
        if di == 'UP':
            if pos[0] == 0 and pos[1] != len(matrix[0]) - 1:
                di = 'DOWN'
                pos = [pos[0], pos[1] + 1]
            elif pos[1] == len(matrix[0]) - 1:
                di = 'DOWN'
                pos = [pos[0] + 1, pos[1]]
            else:
                pos = [pos[0] - 1, pos[1] + 1]
        else:
            if pos[0] == len(matrix) - 1 :
                di = 'UP'
                pos = [pos[0], pos[1] + 1]
            elif pos[1] == 0:
                di = 'UP'
                pos = [pos[0] + 1, pos[1]]
            else:
                pos = [pos[0] + 1, pos[1] - 1]
                
    res.append(matrix[pos[0]][pos[1]])
    return res