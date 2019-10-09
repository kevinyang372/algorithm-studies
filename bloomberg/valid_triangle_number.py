# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].

def triangleNumber(self, nums):
    if len(nums) < 3: return 0
    nums.sort()
    
    res = 0
    for i in range(len(nums) - 2):
        for t in range(i + 1, len(nums) - 1):
            lower = bisect.bisect_right(nums[t + 1:], nums[t] - nums[i])
            upper = bisect.bisect_left(nums[t + 1:], nums[t] + nums[i])
            res += max(upper - lower, 0)
                    
    return res