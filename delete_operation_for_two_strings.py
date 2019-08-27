# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.

def minDistance(self, word1, word2):
    h1, h2 = len(word1) + 1, len(word2) + 1
    mat = [[0] * h1 for _ in range(h2)]
    
    mat[0][0] = 0
    
    for i in range(1, h2):
        for t in range(1, h1):
            if word1[t - 1] == word2[i - 1]:
                mat[i][t] = 1 + mat[i - 1][t - 1]
            else:
                mat[i][t] = max(mat[i - 1][t], mat[i][t - 1])
    
    return h1 + h2 - 2 - 2 * mat[h2 - 1][h1 - 1]