# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

def wordPattern(self, pattern, s):
    if not pattern and s: return False
    if not s and pattern: return False
    if not s and not pattern: return True
    
    sp = s.split(' ')
    
    d = {}
    d2 = {}
    
    c1 = 0
    c2 = 0
    
    for i in range(len(pattern)):
        if pattern[i] in d:
            temp1 = d[pattern[i]]
        else:
            temp1 = c1
            d[pattern[i]] = c1
            c1 += 1
        
        if i >= len(sp):
            return False
        elif sp[i] in d2:
            temp2 = d2[sp[i]]
        else:
            temp2 = c2
            d2[sp[i]] = c2
            c2 += 1
            
        if temp1 != temp2: return False
        
    if i < len(sp) - 1:
        return False
    return True