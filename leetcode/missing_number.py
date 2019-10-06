# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# O(N) Time O(1) Space
def missingNumber(self, nums):
        
    t = (len(nums) + 1) * len(nums) / 2
    for i in nums:
        t -= i
        
    return t

'''
Bit Manipulation
XOR is communitive
n ^ n = 0
e.g. we have 0 ~ 4 missing 2
The following calculates:
4 ^ (0 ^ 0) ^ (1 ^ 1) ^ (2 ^ 3) ^ (3 ^ 4)
= (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ (4 ^ 4) ^ 2
= 2
'''
def missingNumber(self, nums):
        
    t = len(nums)
    for i, v in enumerate(nums):
        t ^= (i ^ v)
        
    return t

