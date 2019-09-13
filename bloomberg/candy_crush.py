# Given a string, reduce the string by removing 3 or more consecutive identical characters.

# Example 1:

# Input: "aaabbbc"
# Output: "c"
# Example 2:

# Input: "aabbbacd"
# Output: "cd"

def candyCrush(s):

    if len(s) < 3: return s

    i, j = 0, 1
    res = ''

    while i < len(s):

        while j < len(s) and s[i] == s[j]:
            j += 1

        if j - i < 3:
            res += s[i] * (j - i)

        i = j
        j = i + 1

    return res
