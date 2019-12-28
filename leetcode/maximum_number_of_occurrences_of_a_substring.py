# Given a string s, return the maximum number of ocurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
 

# Example 1:

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 ocurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
# Example 2:

# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
# Example 3:

# Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# Output: 3
# Example 4:

# Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# Output: 0
 

# Constraints:

# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s only contains lowercase English letters.

def maxFreq(self, s, maxLetters, minSize, maxSize):
        
    if len(s) < minSize: return 0
    
    res = 0
    for l in range(minSize, maxSize + 1):
        i, j = 0, l
        c = collections.Counter(s[i:j])

        max_len = 0
        d = collections.Counter()
        
        while j <= len(s):
            
            if len(c) <= maxLetters:
                d[s[i:j]] += 1
                max_len = max(max_len, d[s[i:j]])
                
            c[s[i]] -= 1
            if c[s[i]] == 0:
                c.pop(s[i])
            
            if j < len(s):
                c[s[j]] += 1
                
            i += 1
            j += 1
        
        res = max(res, max_len)
        if res > 0: return res
    
    return res