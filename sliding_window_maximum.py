# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# monotonic queue
def maxSlidingWindow(self, nums, k):
        
    if not nums: return []
    
    start = []
    for i in nums[:k]:
        if not start or i > -start[0]:
            start = [-i]
        else:
            ind = bisect.bisect_right(start, -i)
            start = start[:ind] + [-i]
            
    res = [-start[0]]
    
    for i in range(k, len(nums)):
        if nums[i - k] == -start[0]:
            start.pop(0)
        if not start or nums[i] > -start[0]:
            start = [-nums[i]]
        else:
            ind = bisect.bisect_right(start, -nums[i])
            start = start[:ind] + [-nums[i]]
        res.append(-start[0])
        
    return res