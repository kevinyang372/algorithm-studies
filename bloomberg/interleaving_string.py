# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example 1:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def isInterleave(self, s1, s2, s3):
        if (s1, s2, s3) in self.cache: return self.cache[s1, s2, s3]
        if len(s1) + len(s2) != len(s3): return False
        if not s1 and not s2 and not s3: return True
        
        if not s1:
            res = s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:])
        elif not s2:
            res =  s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:])
        else:
            res = (s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:])) or (s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]))
        
        self.cache[s1, s2, s3] = res
        return res