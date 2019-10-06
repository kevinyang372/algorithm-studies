# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# dp memoization
class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def numDecodings(self, s):
        if s in self.cache: return self.cache[s]
        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return 1
        
        res = 0
        if int(s[0]) > 2 or (int(s[0]) == 2 and int(s[1]) > 6):
            res = self.numDecodings(s[1:])
        elif len(s[2:]) == 0:
            res = self.numDecodings(s[1:]) + 1
        else:
            res = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            
        self.cache[s] = res
        return res