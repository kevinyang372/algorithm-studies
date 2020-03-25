# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

# If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^5

def sumFourDivisors(self, nums: List[int]) -> int:
        
    def find_all_primes(n):
        if n < 2: return set()
        prime = [True] * (n - 1)
        
        for i in range(len(prime) // 2 + 1):
            if prime[i]:
                curr = i + 2
                for m in range(2 * curr, len(prime) + 2, curr):
                    prime[m - 2] = False
            
        return set(i + 2 for i in range(len(prime)) if prime[i])
    
    d = find_all_primes(max(nums))
    search = sorted(list(d))
    res = 0
    
    for num in nums:
        for prime in search:
            if prime >= math.sqrt(num):
                break
            elif num % prime == 0 and (num // prime in d or prime ** 3 == num):
                res += 1 + num + prime + num // prime
                break
    
    return res