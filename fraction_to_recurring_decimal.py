# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

def fractionToDecimal(numerator, denominator):
    if denominator == 0: return False
    
    sign = '-' if numerator * denominator < 0 else ''
    whole, remainder = divmod(abs(numerator), abs(denominator))
    
    res = [sign + str(whole), '.']
    stack = []
    
    while remainder not in stack:
        stack.append(remainder)
        whole, remainder = divmod(remainder * 10, abs(denominator))
        res.append(str(whole))
        
    ind = stack.index(remainder)
    res.insert(ind + 2, '(')
    res.append(')')
    
    return ''.join(res).replace('(0)', '').rstrip('.')