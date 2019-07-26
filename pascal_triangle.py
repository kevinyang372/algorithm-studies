# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(self, numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1], [1,1]]
    
    root = [[1], [1,1]]
    i = 2
    while i < numRows:
        temp = [1] + [root[-1][t] + root[-1][t + 1] for t in range(0, len(root[-1]) - 1)] + [1]
        root.append(temp)
        i += 1
    
    return root