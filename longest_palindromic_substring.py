# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s: str) -> str:

    if len(s) < 1:
        return s

    i = 0
    j = len(s) - 1
    palindrome = True

    while i <= j:

        if s[i] != s[j]:
            palindrome = False
            break

        i += 1
        j -= 1

    if palindrome:
        return s
    else:
        p1 = longestPalindrome(s[1:])
        p2 = longestPalindrome(s[:-1])

        return p1 if len(p1) > len(p2) else p2