# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

def findDuplicates(self, nums):
        
    res = []
    seen = set()
    
    for i, v in enumerate(nums):
        nums[abs(v) - 1] = -nums[abs(v) - 1]
        seen.add(abs(v))
        
    for i in range(len(nums)):
        if nums[i] > 0 and i + 1 in seen:
            res.append(i + 1)
    
    return res