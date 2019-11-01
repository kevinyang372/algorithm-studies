# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

def isIsomorphic(self, s, t):
    d1 = {}
    visited = set()
    
    for i in range(len(s)):
        if (s[i] in d1 and d1[s[i]] != t[i]) or (s[i] not in d1 and t[i] in visited):
            return False
        elif s[i] not in d1:
            d1[s[i]] = t[i]
            visited.add(t[i])
    
    return True