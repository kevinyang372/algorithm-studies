# Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

# A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

# Example 1:

# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
 

# Constraints:

# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length

# memoization
class Solution(object):
    
    def __init__(self):
        self.cache = {}
    
    def isValidPalindrome(self, s, k):
        if (s, k) in self.cache: return self.cache[s, k]
        if k == 0: return s == s[::-1]
        if not s: return True
        
        i, j = 0, len(s) - 1
        res = True
        while i < j:
            if s[i] != s[j]:
                res = self.isValidPalindrome(s[i:j], k - 1) or self.isValidPalindrome(s[i + 1:j + 1], k - 1)
                break
            else:
                i += 1
                j -= 1
        
        
        self.cache[s, k] = res
        return res

def isValidPalindrome(self, s, k):
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    reverse = s[::-1]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):
            if s[i - 1] == reverse[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return len(s) - dp[-1][-1] <= k
