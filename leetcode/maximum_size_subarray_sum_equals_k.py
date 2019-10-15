# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:

# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?

def maxSubArrayLen(self, nums, k):
        
    v_i = {}
    i_v = {}
    
    sums = 0
    v_i[0] = 0
    for i, v in enumerate(nums):
        sums += v
        i_v[i + 1] = sums
        if sums not in v_i:
            v_i[sums] = i + 1
    
    max_l = 0
    for ind in range(len(nums) - 1, -1, -1):
        cur = i_v[ind + 1]
        if cur - k in v_i:
            max_l = max(max_l, ind - v_i[cur - k] + 1)
            
    return max_l