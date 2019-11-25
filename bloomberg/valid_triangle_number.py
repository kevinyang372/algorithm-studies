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

# TLE two pointers
def triangleNumber(self, nums: List[int]) -> int:
        
    if len(nums) < 3: return 0
    
    nums.sort()
    c = 0
    
    for t in range(len(nums) - 1, 1, -1):
        i, j = 0, 1
        while j < t:
            if nums[i] + nums[j] <= nums[t]:
                j += 1
                if j == t:
                    i += 1
                    j = i + 1
            else:
                c += t - j
                i += 1
                j = i + 1
                
    return c

# binary search
def triangleNumber(self, nums: List[int]) -> int:
    
    if len(nums) < 3: return 0
    
    nums.sort()
    c = 0
    
    for t in range(len(nums) - 1, 1, -1):
        for i in range(t - 1):
            j = i + bisect.bisect_right(nums[i + 1:t - 1], nums[t] - nums[i]) + 1
            if j < t and nums[j] + nums[i] > nums[t]:
                c += t - j
                
    return c