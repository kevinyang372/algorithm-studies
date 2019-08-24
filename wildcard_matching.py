# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

# Recursive TLE
def isMatch(self, s, p):
        
    if s == p: return True
    if len(s) > len(p):
        s, p = p, s
        
    if not s:
        if not p:
            return True
        elif p[0] != '*':
            return False
        else:
            return self.isMatch(s, p[1:])
        
    if s[0] != '*' and s[0] != '?' and p[0] != '*' and p[0] != '?':
        if s[0] != p[0]: return False
        return self.isMatch(s[1:], p[1:])
    elif s[0] == '*' or p[0] == '*':
        
        s1 = s if s[0] == '*' else p
        p1 = p if s1 == s else s
        
        if s[0] == p[0] or p1[0] == '?':
            return self.isMatch(s[1:], p[1:])
        else:
            i = 0
            while i <= len(p1):
                if self.isMatch(s1[1:], p1[i:]):
                    return True
                i += 1
            return False
    else:
        return self.isMatch(s[1:], p[1:])


# dp approach O(M * N)
def isMatch(self, s, p):
    if s == p: return True
    lookup = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    
    lookup[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            lookup[i][0] = lookup[i - 1][0]
        else:
            break
    
    for m in range(1, len(p) + 1):
        for n in range(1, len(s) + 1):
            if p[m - 1] == s[n - 1] or p[m - 1] == '?' or s[n - 1] == '?':
                lookup[m][n] = lookup[m - 1][n - 1]
            elif s[n - 1] == '*':
                lookup[m][n] = lookup[m][n - 1]
            elif p[m - 1] == '*':
                lookup[m][n] = lookup[m][n - 1] or lookup[m - 1][n]
            
    return lookup[len(p)][len(s)]