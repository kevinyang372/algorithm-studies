# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
 

# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9

def minFlips(self, a, b, c):
        
    num_flip = 0
    while a > 0 or b > 0 or c > 0:
        
        fa, fb, fc = (a & 1, b & 1, c & 1)
        if fa | fb != fc:
            if fc == 0 and fa & fb == 1:
                num_flip += 2
            else:
                num_flip += 1
        
        c = c >> 1
        a = a >> 1
        b = b >> 1
    
    return num_flip