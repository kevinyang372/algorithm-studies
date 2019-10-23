# Given a picture consisting of black and white pixels, find the number of black lonely pixels.

# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example:
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]

# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
# Note:
# The range of width and height of the input 2D array is [1,500].

def findLonelyPixel(self, picture):
        
    row = collections.Counter()
    col = collections.Counter()
    visited = set()
    
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == 'B':
                row[i] += 1
                col[j] += 1
                visited.add((i, j))
         
    res = 0
    for x, y in visited:
        if row[x] == 1 and col[y] == 1:
            res += 1
    
    return res