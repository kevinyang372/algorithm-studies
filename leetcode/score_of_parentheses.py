# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6
 

# Note:

# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50

def scoreOfParentheses(self, S):
    stack = 0
    res = 0
    prev = None

    for i in S:
        if i == '(':
            stack += 1
            prev = 1
        else:
            stack -= 1
            if prev == 1:
                res += 2 ** stack
            prev = 0

    return res