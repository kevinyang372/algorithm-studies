# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):

    if len(nums) == 1:
        return nums[0]
    
    return max(sum(nums), maxSubArray(nums[1:]), maxSubArray(nums[:-1]))


def maxSubArray_dp(nums):

    memoize = [["" for i in range(len(nums))] for t in range(len(nums))]

    return maxSubArray_memoize(memoize, nums, [0, len(nums) - 1])

def maxSubArray_memoize(lookup, nums, loc):

    if len(nums) == 1:
        return nums[0]
    elif lookup[loc[0]][loc[1]] != "":
        result = lookup[loc[0]][loc[1]]
    else:
        result = max(sum(nums), maxSubArray_memoize(lookup, nums[1:], [loc[0] + 1, loc[1]]), maxSubArray_memoize(lookup, nums[:-1], [loc[0], loc[1] - 1]))
        lookup[loc[0]][loc[1]] = result
    
    return result

def maxSubArray_true(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

# prefix sum
def maxSubArray(self, nums: List[int]) -> int:
    minimum = sums = 0
    res = -float('inf')
    
    for num in nums:
        sums += num
        res = max(res, sums - minimum)
        minimum = min(minimum, sums)
        
    return res