# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example 1:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3): return False
        
    d = {}
    def check(p1, p2, p3):
        if (p1, p2, p3) in d: return d[p1, p2, p3]
        if p3 == len(s3): return True
        if p1 < len(s1) and s1[p1] == s3[p3]:
            if check(p1 + 1, p2, p3 + 1):
                d[p1, p2, p3] = True
                return True
        if p2 < len(s2) and s2[p2] == s3[p3]:
            if check(p1, p2 + 1, p3 + 1):
                d[p1, p2, p3] = True
                return True
        d[p1, p2, p3] = False
        return False
        
    return check(0, 0, 0)