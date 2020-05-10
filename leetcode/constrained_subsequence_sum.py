# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

# Example 1:

# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# Example 2:

# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.
# Example 3:

# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
 

# Constraints:

# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# TLE
def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
    dp = [0] * len(nums)
    max_num = -float('inf')
    
    for j in range(len(nums) - 1, -1, -1):
        dp[j] = nums[j]
        for i in range(1, k + 1):
            if j + i >= len(nums): break
            dp[j] = max(dp[j], nums[j] + dp[j + i])
        max_num = max(max_num, dp[j])
        
    return max_num

# max sliding window
def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
    max_num = -float('inf')
    q = collections.deque()
    
    for j in range(len(nums) - 1, -1, -1):
        while q and q[0][1] - j > k: q.popleft()
        
        curr = nums[j]
        if q: curr = max(curr, curr + q[0][0])
            
        while q and q[-1][0] <= curr: q.pop()
        q.append((curr, j))
        
        max_num = max(max_num, curr)
        
    return max_num