# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

def findMin(self, nums):
    if nums[0] <= nums[-1]: return nums[0]
    
    lower, upper = 0, len(nums)
    while lower < upper:
        mid = (lower + upper) // 2
        if nums[mid] <= nums[-1]:
            upper = mid
        else:
            lower = mid + 1
         
    res = nums[mid]
    if mid + 1 < len(nums):
        res = min(nums[mid], nums[mid + 1])
        
    return res