# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

def findShortestSubArray(self, nums):
        
    start, end, c = {}, {}, collections.Counter()
    max_val = []
    
    for i, v in enumerate(nums):
        
        end[v] = i
        curr = c[v] + 1
        
        if v not in start:
            start[v] = i
        if not max_val or curr > c[max_val[0]]:
            max_val = [v]
        elif curr == c[max_val[0]]:
            max_val.append(v)
        
        c[v] = curr
        
    return min([end[i] - start[i] + 1 for i in max_val])