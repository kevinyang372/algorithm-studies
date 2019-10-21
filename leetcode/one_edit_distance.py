# Given two strings s and t, determine if they are both one edit distance apart.

# Note: 

# There are 3 possiblities to satisify one edit distance apart:

# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:

# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.

def isOneEditDistance(self, s, t):
        
    if s == t: return False
    
    if len(s) > len(t):
        s, t = t, s
        
    l1 = len(s)
    l2 = len(t)
    
    if abs(l1 - l2) > 1: return False
    
    i = 0
    while i < l1:
        if s[i] != t[i]:
            if l1 == l2:
                return s[i + 1:] == t[i + 1:]
            else:
                return s[i:] == t[i + 1:]
        i += 1
        
    return True