# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
 

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

def countSubstrings(s):

    if len(s) == 0: return []

    count = [[0] * len(s) for _ in range(len(s))]
    total = 0

    for m in range(len(s)):
        for n in range(m, -1, -1):
            if m == n:
                count[m][n] = 1
            elif m - n == 1:
                count[m][n] = 1 if s[m] == s[n] else 0
            else:
                count[m][n] = 1 if s[m] == s[n] and count[m - 1][n + 1] == 1 else 0

            if count[m][n] == 1:
                total += 1

    return total
