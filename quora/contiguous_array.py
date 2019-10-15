# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

def findMaxLength(self, nums):
    d = {}
    n0 = n1 = 0
    d[0] = -1
    
    max_length = -float('inf')
    for i, v in enumerate(nums):
        if v == 0:
            n0 += 1
        else:
            n1 += 1
        
        d[n1 - n0] = min(i, d.get(n1 - n0, float('inf')))
        
        if n1 - n0 in d:
            max_length = max(max_length, i - d[n1 - n0])
            
    return max_length if max_length != -float('inf') else 0