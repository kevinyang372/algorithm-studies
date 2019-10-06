# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

def minDistance(word1, word2):

    if word1 == "":
        return len(word2)
    elif word2 == "":
        return len(word1)
    elif word1[-1] == word2[-1]:
        cost = 0
    else:
        cost = 1

    cost += min(minDistance(word1[:-1], word2), minDistance(word2[:-1], word1), minDistance(word1[:-1], word2[:-1]))
    return cost

# Levenshtein Distance
def minDistance_dp(word1, word2):

    if word1 == "":
        return len(word2)
    elif word2 == "":
        return len(word1)

    mat = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    for m in range(len(word2) + 1):
        for n in range(len(word1) + 1):
            if m == 0:
                mat[m][n] = n
            elif n == 0:
                mat[m][n] = m
            elif word1[n - 1] == word2[m - 1]:
                mat[m][n] = mat[m - 1][n - 1]
            else:
                mat[m][n] = min(mat[m - 1][n], mat[m][n - 1], mat[m - 1][n - 1]) + 1

    return mat[len(word2)][len(word1)]