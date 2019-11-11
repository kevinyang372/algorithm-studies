# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".

# LCS approach
def longestPalindromeSubseq(self, s):
        
    if not s: return 0
    
    s2 = s[::-1]
    dp = [[0] * (len(s) + 1) for _ in range(len(s2) + 1)]
    
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s) + 1):
            if s[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                
    return dp[-1][-1]