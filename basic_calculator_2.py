# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5
# Note:

# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

def calculate(s):

    s = s.replace(' ', '')

    if not s: 
        return 0
    if s.isdigit():
        return int(s)

    start = -1
    end = -1
    trans = {ord('+'): ord('-'), ord('-'): ord('+')}

    for k, v in enumerate(s):
        if v == '+':
            return calculate(s[:k]) + calculate(s[k + 1:])
        elif v == '-':
            return calculate(s[:k]) - calculate(s[k + 1:].translate(trans))
        elif v == '*' or v == '/':
            temp = k + 1
            while s[temp].isdigit() and temp < len(s):
                temp += 1

            if v == '*':
                curr = int(s[:k]) * int(s[k + 1:temp])
            else:
                curr = int(s[:k]) / int(s[k + 1:temp])
                
            return calculate(str(curr) + s[temp:])


# stack

def calculate(s):

    num, stack, sign = 0, [], "+"

    for k, v in enumerate(s):
        if v.isdigit():
            num = num * 10 + int(v)
        if v in "+-*/" or k == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(stack.pop() // num)

            sign = v
            num = 0

    return sum(stack)


