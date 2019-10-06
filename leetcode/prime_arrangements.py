# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.

 

# Example 1:

# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
# Example 2:

# Input: n = 100
# Output: 682289015
 

# Constraints:

# 1 <= n <= 100

def numPrimeArrangements(self, n):
    to_mod = 10 ** 9 + 7
    
    def count(n):
        
        if n < 2: return 0
        
        filled = [1] * n
        filled[0] = 0
        filled[1] = 0
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if filled[i] == 1:
                for j in range(i * i, n, i):
                    filled[j] = 0
        
        return sum(filled)
    
    res = count(n + 1)
    return math.factorial(res) * math.factorial(n - res) % to_mod