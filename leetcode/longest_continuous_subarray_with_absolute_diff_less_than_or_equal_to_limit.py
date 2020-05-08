# Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

# In case there is no subarray satisfying the given condition return 0.

 

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9

def longestSubarray(self, nums: List[int], limit: int) -> int:
        
    max_len = 0
    i = 0
    
    minimum = collections.deque()
    maximum = collections.deque()
    
    for j in range(len(nums)):
        while maximum and maximum[-1] < nums[j]: maximum.pop()
        while minimum and minimum[-1] > nums[j]: minimum.pop()
            
        maximum.append(nums[j])
        minimum.append(nums[j])
        
        while maximum[0] - minimum[0] > limit:
            if nums[i] == maximum[0]: maximum.popleft()
            if nums[i] == minimum[0]: minimum.popleft()
            
            i += 1
        
        max_len = max(max_len, j - i + 1)
    
    return max_len