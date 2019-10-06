# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# Example 1:

# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: "abcd"
# Output: "dcbabcd"

# TLE
def shortestPalindrome(self, s):
        
    stack = []
    maxCount = 0
    for i in range(len(s)):
        stack.append(s[i])
        if stack == stack[::-1]:
            maxCount = max(maxCount, len(stack))
            
    return s[maxCount:][::-1] + s[:maxCount] + s[maxCount:]

def shortestPalindrome(self, s):
    n = len(s)
    l, r = s, ""
    rev_s = s[::-1]
    
    while(rev_s != r + l and n > 1):
        r += l[-1]
        l = l[:n - 1]
        n -= 1
    return r + s