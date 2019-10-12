# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].

# TLE
def checkValidString(s, score = 0):

    if not s:
        if score == 0:
            return True
        else:
            return False
    if score < 0: return False

    if s[0] == '(':
        return checkValidString(s[1:], score + 1)
    elif s[0] == ')':
        return checkValidString(s[1:], score - 1)
    else:
        return checkValidString(s[1:], score + 1) or checkValidString(s[1:], score - 1) or checkValidString(s[1:], score)
