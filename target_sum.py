# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

# TLE
def findTargetSumWays(nums, S):

    stack = [0]

    for i in nums:
        stack = [x + i for x in stack] + [x - i for x in stack]
    
    return stack.count(S)

# Backtracking TLE
def findTargetSumWays(nums, S):

    if not nums:
        if S == 0:
            return 1
        else:
            return 0

    count = 0

    for i in [nums[0], -nums[0]]:
        count += findTargetSumWays(nums[1:], S - i)

    return count

# Backtracking memoization
cache = collections.Counter()
    
def findTargetSumWays(self, nums, S, ind = 0):
    
    if (ind, S) in cache: return cache[(ind, S)]
    
    if ind >= len(nums):
        if S == 0:
            return 1
        else:
            return 0
        
    count = 0

    for i in [nums[ind], -nums[ind]]:
        count += self.findTargetSumWays(nums, S - i, ind + 1)
        
    cache[(ind, S)] += count
    return count