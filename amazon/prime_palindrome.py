# Find the smallest prime palindrome greater than or equal to N.

# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

# For example, 2,3,5,7,11 and 13 are primes.

# Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

# For example, 12321 is a palindrome.

 

# Example 1:

# Input: 6
# Output: 7
# Example 2:

# Input: 8
# Output: 11
# Example 3:

# Input: 13
# Output: 101
 

# Note:

# 1 <= N <= 10^8
# The answer is guaranteed to exist and be less than 2 * 10^8.

# Sieve of Eratosthenes
def primePalindrome(self, N):
        
    MAX = N ** 2
    nums = [True] * MAX
    nums[0] = False
    nums[1] = False
    
    i = 2
    while i < len(nums):
        if not i:
            i += 1
        else:
            for t in range(2 * i, MAX, i):
                nums[t] = False
            i += 1
    
    def checkPalindrome(num):
        return str(num) == str(num)[::-1]
        
    for t in range(N, MAX):
        if nums[t] and checkPalindrome(t):
            return t