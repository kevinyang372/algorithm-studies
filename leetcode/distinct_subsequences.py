# Given a string S and a string T, count the number of distinct subsequences of S which equals T.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Example 1:

# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:

# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:

# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:

# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

# O(N^3)
def numDistinct(self, s: str, t: str) -> int:
        
    if len(t) == 1: return s.count(t)
    
    dp = [[] for _ in range(len(s))]
    count = 0
    
    for i, v in enumerate(s):
        if v == t[0]: dp[i].append(0)
        for p in range(i):
            for m in dp[p]:
                if v == t[m + 1]:
                    if m + 1 == len(t) - 1:
                        count += 1
                    else:
                        dp[i].append(m + 1)
    
    return count

# Dynamic Programming
def numDistinct(self, s: str, t: str) -> int:
        
    if len(t) == 1: return s.count(t)
    
    dp = [[0] * len(s) for _ in range(len(t))]
    
    sums = 0
    for i in range(len(dp[0])):
        if s[i] == t[0]:
            sums += 1
        dp[0][i] = sums
         
    for m in range(1, len(t)):
        for n in range(m, len(s)):
            if s[n] == t[m]:
                dp[m][n] = min(dp[m][n - 1] + dp[m - 1][n - 1], math.factorial(n + 1) // (math.factorial(m + 1) * max(1, math.factorial(n - m))))
            else:
                dp[m][n] = dp[m][n - 1]
    
    return dp[-1][-1]