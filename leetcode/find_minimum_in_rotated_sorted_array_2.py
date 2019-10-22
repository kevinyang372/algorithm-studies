# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

def findMin(self, nums):
    if not nums: return float('inf')
    if len(nums) == 1: return nums[0]
    if nums[0] < nums[-1]: return nums[0]

    lower, upper = 0, len(nums) - 1
    while lower < upper:
        mid = (lower + upper) // 2
        if nums[mid] < nums[-1]:
            upper = mid
        elif nums[mid] == nums[-1]:
            return min(self.findMin(nums[lower:mid]), self.findMin(nums[mid + 1:upper + 1]))
        else:
            lower = mid + 1

    res = nums[mid]
    if mid + 1 < len(nums):
        res = min(nums[mid], nums[mid + 1])

    return res