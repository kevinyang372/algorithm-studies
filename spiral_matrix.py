# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(self, matrix):
    if not matrix: return
    
    res = []
    i = 0
    w = len(matrix[0])
    h = len(matrix)
    
    while True:
        if i < w - i:
            res += matrix[i][i:w - i]
        else:
            break
        if i < h - i - 1:
            res += [matrix[t][w - i - 1] for t in range(i + 1, h - i - 1)]
        else:
            break
        
        res += matrix[h - i - 1][i:w - i][::-1]
        
        if i != w - i - 1 and h - i - 2 > i:
            res += [matrix[t][i] for t in range(h - i - 2, i, -1)]
        else:
            break
            
        i += 1
        
    return res