# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:

# You can assume that you can always reach the last index.

# TLE
def jump(self, nums):
        
    d = [float('inf')] * len(nums)
    d[0] = 0
    
    for i in range(len(nums) - 1):
        for t in range(1, nums[i] + 1):
            if i + t >= len(nums): break
            d[i + t] = min(d[i + t], 1 + d[i])
        
    return d[-1]

# bfs 
def jump(self, nums):

    if len(nums) <= 1: return 0

    left, right = 0, nums[0]
    times = 1
    
    while right < len(nums) - 1:
        times += 1
        nxt = max([i + nums[i] for i in range(left, right + 1)])
        left, right = right, nxt
        
    return times