# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

# Note:
# If n is the length of array, assume the following constraints are satisfied:

# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:

# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# TLE backtracking + memoization
def splitArray(self, nums, m):
        
    cache = {}
    def traverse(ind, i):
        if (ind, i) in cache: return cache[ind, i]
        if i == 1: 
            res = sum(nums[ind:])
            cache[ind, i] = res
            return res
        
        min_sums = float('inf')
        for t in range(ind + 1, len(nums) - i + 2):
            min_sums = min(max(sum(nums[ind:t]), traverse(t, i - 1)), min_sums)
            
        cache[ind, i] = min_sums
        return min_sums
    
    return traverse(0, m)