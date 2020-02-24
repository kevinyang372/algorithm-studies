# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.

def numberOfSubstrings(self, s: str) -> int:
        
    d = collections.defaultdict(list)
    for i, v in enumerate(s):
        d[v].append(i)
        
    d['a'].append(len(s))
    d['b'].append(len(s))
    d['c'].append(len(s))
        
    i = j = k = c = 0
    for ind in range(len(s)):
        c += len(s) - max(d['a'][i], d['b'][j], d['c'][k])
        if s[ind] == 'a':
            i += 1
        elif s[ind] == 'b':
            j += 1
        else:
            k += 1
    
    return c