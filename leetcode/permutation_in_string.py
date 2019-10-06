# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

# sliding window
def checkInclusion(self, s1, s2):
    if len(s1) > len(s2): return False
    if len(s1) == 1: return s1 in s2
    
    d = collections.Counter(s1)
    m = collections.Counter(s2[:len(s1)])
    
    if d == m: return True
    
    for i in range(len(s1), len(s2)):
        if m[s2[i - len(s1)]] == 1:
            m.pop(s2[i - len(s1)])
        else:
            m[s2[i - len(s1)]] -= 1
            
        m[s2[i]] += 1
        if d == m: return True
            
    return False