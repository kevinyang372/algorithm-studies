# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

import math

cache = {}

def numSquares(n):

    if n in cache: return cache[n]

    sq = math.sqrt(n)

    if sq % 1 == 0: return 1

    num = 1 + numSquares(n - 1)

    for i in range(2, int(sq) + 1):
        num = min(1 + numSquares(n - i**2), num)

    cache[n] = num

    return num


