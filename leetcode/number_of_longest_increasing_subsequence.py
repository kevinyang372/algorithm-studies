# Given an integer array nums, return the number of longest increasing subsequences.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

# Constraints:

# 0 <= nums.length <= 2000
# -106 <= nums[i] <= 106

def findNumberOfLIS(self, nums: List[int]) -> int:
    dp = [[1, 1]] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[i][0] < dp[j][0] + 1:
                    dp[i] = [dp[j][0] + 1, dp[j][1]]
                elif dp[i][0] == dp[j][0] + 1:
                    dp[i][1] += dp[j][1]
    
    max_val = -float('inf')
    max_count = 0
    
    for i in range(len(dp)):
        if dp[i][0] > max_val:
            max_count = dp[i][1]
            max_val = dp[i][0]
        elif dp[i][0] == max_val:
            max_count += dp[i][1]
    
    return max_count