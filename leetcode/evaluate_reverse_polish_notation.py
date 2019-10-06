# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

def evalRPN(self, tokens):
    if len(tokens) < 2: return tokens[0]
    
    stack = [int(i) for i in tokens[:2]]
    i = 2
    
    while i < len(tokens) or len(stack) > 1:
        if tokens[i] not in "+-*/":
            stack.append(int(tokens[i]))
            i += 1
        else:
            a = stack.pop()
            b = stack.pop()
            
            if tokens[i] == "+":
                res = a + b
            elif tokens[i] == "*":
                res = a * b
            elif tokens[i] == "-":
                res = b - a
            else:
                res = int(float(b) / a)
            stack.append(res)
            i += 1
    
    return stack[0]