# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true

def isValid(s: str):

    stack = []

    for i in s:
        if i in ['(', '[', '{']:
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            num = stack.pop()
            if num != '(':
                return False
        elif i == ']':
            if len(stack) == 0:
                return False
            num = stack.pop()
            if num != '[':
                return False
        elif i == '}':
            if len(stack) == 0:
                return False
            num = stack.pop()
            if num != '{':
                return False

    if len(stack) != 0:
        return False

    return True
