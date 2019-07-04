# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# Recursive TLE
def isvalid(s):
    return s == s[::-1]

def validPalindrome(s):

    if isvalid(s): return True

    for i in range(len(s)):
        if isvalid(s[:i] + s[i + 1:]):
            return True

    return False

# Faster two pointer
def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            m, n = s[left:right], s[left + 1: right + 1]
            return m == m[::-1] or n == n[::-1]
        left += 1
        right -= 1
    return True