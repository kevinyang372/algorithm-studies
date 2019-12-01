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

# monotonic queue O(N)
class MonotonicQueue:
    def __init__(self):
        self.q = collections.deque()
        
    def push(self, ele):
        if not self.q:
            self.q.append([ele, 0])
            return
        
        count = 0
        while self.q and self.q[-1][0] < ele:
            _, num = self.q.pop()
            count += num + 1
        
        self.q.append([ele, count])
    
    def pop(self):
        if self.q[0][1] == 0:
            self.q.popleft()
        else:
            self.q[0][1] -= 1
    
    def max(self):
        return self.q[0][0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums: return
        if k == 1: return nums
        
        d = MonotonicQueue()
        
        for i in range(k):
            d.push(nums[i])
        
        res = []
        res.append(d.max())
        
        ind = k
        while ind < len(nums):
            d.pop()
            d.push(nums[ind])
            res.append(d.max())
            ind += 1
            
        return res


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