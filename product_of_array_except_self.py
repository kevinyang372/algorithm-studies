# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

def productExceptSelf(nums):

    p = [1] * len(nums)

    for i in reversed(range(len(nums) - 1)):
        p[i] = nums[i + 1] * p[i + 1]

    pre = 1
    for i in range(1, len(nums)):
        pre *= nums[i - 1]
        p[i] = p[i] * pre

    return p