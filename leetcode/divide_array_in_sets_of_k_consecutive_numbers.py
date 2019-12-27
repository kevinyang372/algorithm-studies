# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.

 

# Example 1:

# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:

# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:

# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# Example 4:

# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
 

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length

def isPossibleDivide(self, nums, k):
    if len(nums) % k > 0: return False
    
    c = collections.Counter(nums)
    s = sorted(c.keys())
    
    i = j = count = 0
    
    while count < len(nums):
        
        j = i
        
        for dj in range(k):
            if s[j] + dj not in c or c[s[j] + dj] <= 0: return False
            
            c[s[j] + dj] -= 1
            count += 1
            
            if s[j] + dj == s[i] and c[s[j] + dj] == 0:
                i += 1
    
    return True