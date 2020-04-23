# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4
# Example 2:

# Input: [0,1]
# Output: 0

# TLE
def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
    curr = m
    while curr != 0 and m < n:
        curr &= m + 1
        m += 1
    
    return curr

# O(logN)
def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1

    return n << i