# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

def repeatedSubstringPattern(self, s: str) -> bool:
    i = 1
    while i <= len(s) // 2:
        if s[i] == s[0] and len(s) % i == 0 and s.count(s[:i]) == len(s) // i:
            return True
        i += 1
    return False

# eliminate pattern one by one
def repeatedSubstringPattern(self, s: str) -> bool:
    curr = []
    pattern = ''
    d = set()
    
    for char in s:
        pattern += char
        
        for ind in range(len(curr)):
            if curr[ind][2]:
                curr[ind][0] += char
                if len(curr[ind][0]) == curr[ind][1]:
                    if curr[ind][0] in d:
                        curr[ind][0] = ''
                    else:
                        curr[ind][2] = False
        
        if len(pattern) != len(s) and len(s) % len(pattern) == 0:
            d.add(pattern)
            curr.append(['', len(pattern), True])

    return any(pat[2] for pat in curr)