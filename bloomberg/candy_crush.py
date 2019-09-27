# Given a string, reduce the string by removing 3 or more consecutive identical characters.

# Example 1:

# Input: "aaabbbc"
# Output: "c"
# Example 2:

# Input: "aabbbacd"
# Output: "cd"

# stack approach
def candyCrush(s):

    if len(s) < 3: return s

    stack = []
    i = 0
    
    while i < len(s):
        if not stack:
            stack.append([s[i], 1])
            i += 1
        elif s[i] == stack[-1][0]:
            stack[-1][1] += 1
            i += 1
        elif stack[-1][1] >= 3:
            stack.pop()
        else:
            stack.append([s[i], 1])
            i += 1
            
    while stack and stack[-1][1] >= 3:
        stack.pop()
    
    return "".join([x * y for x, y in stack])

# recursive approach
def candyCrush(s):

    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        elif j - i >= 3:
            return candyCrush(s[:i] + s[j:])
        else:
            i = j
            j += 1
    return s

# optimial solve
def candyCrush(s):

    i, j = 0, 1
    min_val = s
    while j < len(s):
        if s[i] == s[j]:
            j += 1
            continue
        elif j - i >= 3:
            temp = candyCrush(s[:i] + s[j:])
            min_val = min(temp, min_val, key=len)

        i = j
        j += 1
    return min_val