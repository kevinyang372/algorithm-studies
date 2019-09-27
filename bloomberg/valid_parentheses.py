# Given a string of parentheses:
# s = "()(()()()()())"

# Remove the minimum amount of parentheses to make the string parentheses balanced in-place.

def validParentheses(s):
    if not s: return
    
    stack = []
    count = 0
    for ind, val in enumerate(s):
        if val == ')' and stack and stack[-1][1] == '(':
            stack.pop()
        else:
            stack.append((ind, val))
            
    s = list(s)
    while stack:
        s.pop(stack.pop()[0])
    
    return "".join(s)