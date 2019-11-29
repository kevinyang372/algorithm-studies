# Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

# Example 1:

# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes: 

# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1

def largestOverlap(self, A, B):
        
    dA, dB = set(), set()
    
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i][j] == 1:
                dA.add((i, j))
            if B[i][j] == 1:
                dB.add((i, j))
      
    max_val = 0
    for x, y in dA:
        for m, n in dB:
            dx, dy = x - m, y - n
            count = 0
            for i, j in dA:
                if (i - dx, j - dy) in dB:
                    count += 1
            max_val = max(max_val, count)
            
    return max_val