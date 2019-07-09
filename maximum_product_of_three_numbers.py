# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1,2,3]
# Output: 6
 

# Example 2:

# Input: [1,2,3,4]
# Output: 24
 

# Note:

# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

def maximumProduct(nums):
    if len(nums) == 3: return nums[0] * nums[1] * nums[2]
    
    pos = [0] * 3
    neg = [0] * 3
    
    for i in nums:
        if i > pos[0]:
            pos[0] = i
            pos.sort()
        elif i < neg[0]:
            neg[0] = i
            neg.sort(reverse=True)
    
    return max(pos[0] * pos[1] * pos[2], pos[2] * neg[1] * neg[2])