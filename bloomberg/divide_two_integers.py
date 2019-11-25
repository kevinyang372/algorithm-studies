# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

def divide(self, dividend, divisor):
        
    sign = (dividend > 0) == (divisor > 0)
    
    c = 0
    dividend, divisor = abs(dividend), abs(divisor)
    
    while dividend >= divisor:
        curr = divisor
        i = 1
        while dividend >= curr:
            dividend -= curr
            curr *= 2
            c += 2 ** (i - 1)
            i += 1       
            
    if sign:
        return min(c, 2**31 - 1)
    else:
        return max(-c, -2**31)
