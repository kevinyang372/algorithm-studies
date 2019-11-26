# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.

def longestLine(self, M: List[List[int]]) -> int:
            
    max_val = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                M[i][j] = [0, 0, 0, 0]
            else:
                if j == 0:
                    first = 1
                else:
                    first = M[i][j - 1][0] + 1
                
                if i == 0:
                    second = 1
                    third = 1
                    fourth = 1
                else:
                    second = M[i - 1][j][1] + 1
                    if j > 0:
                        third = M[i - 1][j - 1][2] + 1
                    else:
                        third = 1
                    if j < len(M[0]) - 1:
                        fourth =  M[i - 1][j + 1][3] + 1
                    else:
                        fourth = 1
                
                M[i][j] = [first, second, third, fourth]
                
            max_val = max(max_val, max(M[i][j]))
            
    return max_val