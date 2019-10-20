# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

def maximalRectangle(self, matrix):
        
    if not matrix: return 0
    
    R, C = len(matrix), len(matrix[0])
    cache = [[0 for _ in range(C)] for _ in range(R)]
    max_area = 0
    
    for i in range(R):
        for t in range(C):
            if matrix[i][t] == "1":
                if i == 0:
                    cache[i][t] = 1
                else:
                    cache[i][t] = cache[i - 1][t] + 1
                    
                temp = cache[i][t]
                cur_min = cache[i][t]
                dt = 1
                
                while t - dt >= 0 and matrix[i][t - dt] == "1":
                    cur_min = min(cur_min, cache[i][t - dt])
                    temp = max(temp, (1 + dt) * cur_min)
                    dt += 1
                
                max_area = max(max_area, temp)

    return max_area