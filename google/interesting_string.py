# Given a string s consisting of digits 0-9 and lowercase English letters a-z.

# A string is interesting if you can split it into several substrings, such that each substring starts with a number and this number represents the number of characters after it. Retrun true if string s is intersting, otherwise false.

# Example 1:

# Input: "4g12y6hunter"
# Output: true
# Explanation: We can split it into "4g12y" and "6hunter".
# Example 2:

# Input: "124gray6hunter"
# Output: true
# Explanation: We can divide it into "12", "4gray", "6hunter".
# Example 3:

# Input: "31ba2a"
# Output: false

def interestingString(s, ind = 0):

    if not s: return True
    if not s[0].isdigit(): return False
    if int(s[0]) + ind * 10 + 1 > len(s): return False

    return interestingString(s[int(s[0]) + ind * 10 + 1:]) or interestingString(s[1:], ind = ind * 10 + int(s[0]))