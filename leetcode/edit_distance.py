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

    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j == 0: 
                continue
            elif i == 0: 
                dp[i][j] = dp[i][j - 1] + 1
            elif j == 0: 
                dp[i][j] = dp[i - 1][j] + 1
            elif word1[j - 1] == word2[i - 1]: 
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                
    return dp[-1][-1]