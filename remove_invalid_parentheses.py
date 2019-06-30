# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Example 1:

# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:

# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:

# Input: ")("
# Output: [""]

def removeInvalidParentheses(s):

    level = {s}

    while True:
        valid = filter(isvalid, level)
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


def isvalid(s):

    ind = 0
    for i in s:
        if i == '(':
            ind += 1
        elif i == ')':
            ind -= 1
        if ind < 0:
            return False

    return ind == 0
