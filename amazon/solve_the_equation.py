# Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

# If there is no solution for the equation, return "No solution".

# If there are infinite solutions for the equation, return "Infinite solutions".

# If there is exactly one solution for the equation, we ensure that the value of x is an integer.

# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: "2x=x"
# Output: "x=0"
# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: "x=x+2"
# Output: "No solution"

def solveEquation(self, equation):
        
    p1, p2 = equation.split('=')
    
    def decompose(eq):
        eq = eq.split('+')
        params = [0, 0]
        
        for i in eq:
            temp = i.split('-')
            for ind, val in enumerate(temp):
                if not val:
                    continue
                elif val[-1] == 'x':
                    pre = int(val[:-1]) if len(val) > 1 else 1
                    if ind == 0:
                        params[0] += pre
                    else:
                        params[0] -= pre
                else:
                    if ind == 0:
                        params[1] += int(val)
                    else:
                        params[1] -= int(val)
        
        return params
    
    a1, b1 = decompose(p1)
    a2, b2 = decompose(p2)
    
    if a1 == a2:
        if b1 == b2:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return "x=%s" % str((b1 - b2) / (a2 - a1))