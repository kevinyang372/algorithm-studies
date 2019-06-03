# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generateParenthesis(n: int):

    if n == 0:
        return ""
    elif n == 1:
        return ["()"]

    result = set()

    for i in range(1, n // 2 + 1):

        p1 = generateParenthesis(n - i)
        p2 = generateParenthesis(i)
        
        for m in p1:
            for t in p2:
                result.add("%s%s" % (m, t))
                result.add("%s%s" % (t, m))
                result.add("%s%s%s" % (t[:len(t) // 2], m, t[len(t) // 2:]))
                result.add("%s%s%s" % (m[:len(m) // 2], t, m[len(m) // 2:]))

    return list(result)