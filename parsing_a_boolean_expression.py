# 1106. Parsing A Boolean Expression
# User Accepted: 188
# User Tried: 228
# Total Accepted: 193
# Total Submissions: 311
# Difficulty: Hard
# Return the result of evaluating a given boolean expression, represented as a string.

# An expression can either be:

# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
 

# Example 1:

# Input: expression = "!(f)"
# Output: true
# Example 2:

# Input: expression = "|(f,t)"
# Output: true
# Example 3:

# Input: expression = "&(t,f)"
# Output: false
# Example 4:

# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
 

# Constraints:

# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
# expression is a valid expression representing a boolean, as given in the description.

def parseBoolExpr(expression):

    if expression == 'f': return False
    if expression == 't': return True

    if expression[0] == '!':
        return not parseBoolExpr(expression[2:-1])
    else:
        innerphrase = expression[2:-1]

        count = 0
        stack = 0
        ind = 0
        store = []

        while count < len(innerphrase):
            if innerphrase[count] == '(':
                stack += 1
            elif innerphrase[count] == ')':
                stack -= 1
            elif innerphrase[count] == ',' and stack == 0:
                store.append(innerphrase[ind:count])
                ind = count + 1

            count += 1

        store.append(innerphrase[ind:])

        if expression[0] == '|':
            res = False:
            for i in store:
                res = res or parseBoolExpr(i)
            return res

       res = True:
        for i in store:
            res = res and parseBoolExpr(i)
        return res 