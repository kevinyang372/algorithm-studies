# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note:

# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Example 1:

# Input: 1
# Output: []
# Example 2:

# Input: 37
# Output:[]
# Example 3:

# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# Example 4:

# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

def getFactors(self, n):
        
    factors = []
    while n > 1:
        found = False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
                found = True
                break
        
        if not found:
            factors.append(n)
            break
    
    if len(factors) <= 1: return
    
    def permutationSearch(arr):
        if len(arr) == 1: return [arr]
        
        temp = arr[0]
        res = set()
        
        for i in permutationSearch(arr[1:]):
            res.add(tuple([temp] + i))
            
            for p in range(len(i)):
                i[p] *= temp
                res.add(tuple(sorted(i)))
                i[p] //= temp
            
        return [list(i) for i in res]
    
    return [i for i in permutationSearch(factors) if len(i) > 1]