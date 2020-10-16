# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]: return False
    if target < matrix[0][0] or target > matrix[-1][-1]: return False
    
    low, high = 0, len(matrix)
    
    while low < high:
        mid = (low + high) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            low = mid + 1
        else:
            high = mid
    
    search_index = mid if matrix[mid][0] < target else mid - 1
    
    low, high = 0, len(matrix[0])
    
    while low < high:
        mid = (low + high) // 2
        if matrix[search_index][mid] == target:
            return True
        elif matrix[search_index][mid] > target:
            high = mid
        else:
            low = mid + 1
    
    return False

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0: return False
    
    def binary_search_col(target):
        i, j = 0, len(matrix)
        
        while i < j:
            mid = (i + j) // 2
            if matrix[mid][0] > target:
                j = mid
            else:
                i = mid + 1
        
        return j - 1
    
    def binary_search_row(target, ind):
        i, j = 0, len(matrix[0])
        
        while i < j:
            mid = (i + j) // 2
            if matrix[ind][mid] > target:
                j = mid
            elif matrix[ind][mid] == target:
                return mid
            else:
                i = mid + 1
        
        return -1
    
    ind = binary_search_col(target)
    if ind < 0: return False
    
    return binary_search_row(target, ind) >= 0