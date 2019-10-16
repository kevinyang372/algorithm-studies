# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# Example 1:

# Input: "1 + 1"
# Output: 2
# Example 2:

# Input: " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

def calculate(self, s):
    if not s: return 0
    
    def inner(ind):
        inner_stack = []
        di = ind
        
        while di < len(s):
            if s[di].isdigit():
                start = di
                while di < len(s) - 1 and s[di + 1].isdigit():
                    di += 1
                if not inner_stack:
                    inner_stack.append(int(s[start:di + 1]))
                elif inner_stack[-1] == '-':
                    inner_stack.pop()
                    num = inner_stack.pop()
                    inner_stack.append(num - int(s[start:di + 1]))
                else:
                    inner_stack.pop()
                    num = inner_stack.pop()
                    inner_stack.append(num + int(s[start:di + 1]))
            elif s[di] in '+-':
                inner_stack.append(s[di])
            elif s[di] == '(':
                res, new_i = inner(di + 1)
                
                if not inner_stack:
                    inner_stack.append(res)
                elif inner_stack[-1] == '-':
                    inner_stack.pop()
                    num = inner_stack.pop()
                    inner_stack.append(num - res)
                else:
                    inner_stack.pop()
                    num = inner_stack.pop()
                    inner_stack.append(num + res)
                
                di = new_i
            elif s[di] == ')':
                return inner_stack[-1], di
            di += 1
    
    stack = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            start = i
            while i < len(s) - 1 and s[i + 1].isdigit():
                i += 1
            if not stack:
                stack.append(int(s[start:i + 1]))
            elif stack[-1] == '-':
                stack.pop()
                num = stack.pop()
                stack.append(num - int(s[start:i + 1]))
            else:
                stack.pop()
                num = stack.pop()
                stack.append(num + int(s[start:i + 1]))        
        elif s[i] in '+-':
            stack.append(s[i])
        elif s[i] == '(':
            
            res, ind = inner(i + 1)                
            if not stack:
                stack.append(res)
            elif stack[-1] == '-':
                stack.pop()
                num = stack.pop()
                stack.append(num - res)
            else:
                stack.pop()
                num = stack.pop()
                stack.append(num + res)
            i = ind
        i += 1
    
    return stack[-1]