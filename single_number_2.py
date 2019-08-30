# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3
# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

# bitwise operations
def singleNumber(self, nums):
    x1 = x2 = mask = 0
     
    for i in nums:
        x2 ^= x1 & i
        x1 ^= i
        mask = ~(x1 & x2)
        x2 &= mask
        x1 &= mask

    return x1