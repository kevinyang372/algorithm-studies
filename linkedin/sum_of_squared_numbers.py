# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:

# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
 

# Example 2:

# Input: 3
# Output: False

# two pointers
def judgeSquareSum(self, c: int) -> bool:
    if c < 0: return False
    
    i, j = 0, int(c ** 0.5)
    
    while i <= j:
        if i ** 2 + j ** 2 == c:
            return True
        elif i ** 2 + j ** 2 < c:
            i += 1
        else:
            j -= 1
            
    return False