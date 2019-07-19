# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(self, n):
    if n <= 2: return 0
    
    primes = [2]
    
    for i in range(2, n):
        isprime = True
        for t in primes:
            if i % t == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
            
    return len(primes)

# Sieve of Eratosthenes
import math
def countPrimes(self, n):
    if n < 3: return 0
    
    filled = [1] * n
    filled[0] = 0
    filled[1] = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if filled[i] == 1:
            for j in range(i*i, n, i):
                filled[j] = 0
            
    return sum(filled)