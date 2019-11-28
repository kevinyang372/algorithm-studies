# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):

    if len(nums) < 1: return [[]]

    par = nums[0]

    res = self.subsets(nums[1:])
    full = res[:]

    for i in res:
        full.append(i + [par])

    return full

def subsets(self, nums):
    if not nums: return [[]]
    
    first = nums[0]
    res = self.subsets(nums[1:])
    
    return res + [[first] + t for t in res]