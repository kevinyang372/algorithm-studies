# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

# two pointers
def minSubArrayLen(self, s, nums):
    if not nums: return 0
    
    i = j = 0
    sums = 0
    min_val = float('inf')
    
    while j < len(nums):
        sums += nums[j]
        
        if sums >= s:
            while sums >= s:
                sums -= nums[i]
                i += 1
            min_val = min(j - i + 2, min_val)
        j += 1
    
    return min_val if min_val != float('inf') else 0