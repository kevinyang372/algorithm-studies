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

def longestPalindrome(s:str) -> str:

    length = len(s)
    arr_2d = [[False for _ in range(length)] for _ in range(length)]
    
    max_sub_len = 0
    substring = (0, 0)
    
    # Trivial case
    for i in range(length):
        arr_2d[i][i] = True
    
    # Two chars base case
    for i in range(length-1):
        j = i + 1
        arr_2d[i][j] = s[i] == s[j]
        if arr_2d[i][j] and (2 > max_sub_len):
            max_sub_len = 2
            substring = (i, j)
    
    # General case
    step = 2
    for _ in range(length-2):
        i = 0
        j = i+step
        while (i < length) and (j < length):
            arr_2d[i][j] = (s[i] == s[j]) and arr_2d[i+1][j-1]
            if arr_2d[i][j] and (j-i+1 > max_sub_len):
                max_sub_len = j-i+1
                substring = (i, j)
            i += 1
            j += 1
        step += 1
    return s[substring[0]: substring[1]+1]

# bfs TLE
def longestPalindrome(self, s):
        
    rev = s[::-1]
    stack = [[s, rev]]
    
    while stack:
        s1, s2 = stack.pop(0)
        if s1 == s2:
            return s1
        stack.append([s1[1:], s2[:-1]])
        stack.append([s1[:-1], s2[1:]])
    
    return ""