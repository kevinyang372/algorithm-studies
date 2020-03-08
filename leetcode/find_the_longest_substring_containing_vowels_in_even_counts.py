# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

# Example 1:

# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:

# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:

# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

# Constraints:

# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.

def findTheLongestSubstring(self, s: str) -> int:
        
    maps = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 3,
        'u': 4
    }
    c = [0] * 5
    d = {}
    d[0, 0, 0, 0, 0] = -1
    temp = collections.Counter()
    
    max_val = 0
    for i, v in enumerate(s):
        if v in maps:
            c[maps[v]] += 1
            c[maps[v]] %= 2
            if tuple(c) not in d:
                d[tuple(c)] = i
                
        max_val = max(max_val, i - d[tuple(c)])
    
    return max_val