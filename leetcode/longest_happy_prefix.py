# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

# Given a string s. Return the longest happy prefix of s .

# Return an empty string if no such prefix exists.

 

# Example 1:

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
# Example 2:

# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
# Example 3:

# Input: s = "leetcodeleet"
# Output: "leet"
# Example 4:

# Input: s = "a"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 10^5
# s contains only lowercase English letters.

# MLE
def longestPrefix(self, s: str) -> str:
        
    d = set()
    tp = ''
    
    for i in s:
        tp += i
        if len(tp) != len(s): d.add(tp)
         
    match = ''
    res = ''
    
    for m in reversed(s):
        match = m + match
        if match in d: res = match
            
    return res

# String Hashing
def longestPrefix(self, s: str) -> str:
        
    l, r, res, mod = 0, 0, -1, 10 ** 9 + 7
    for i in range(len(s) - 1):
        l = (l * 128 + ord(s[i])) % mod
        r = (r + pow(128, i, mod) * ord(s[~i])) % mod
        if l == r: res = i
            
    return s[:res + 1]