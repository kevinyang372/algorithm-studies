# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

def canPartition(nums):

    if not nums:
        return False

    array_sum = sum(nums)

    if array_sum % 2 != 0:
        return False

    target = array_sum // 2

    mat = [0] * (array_sum + 1)
    mat[0] = 1

    for num in nums:
        for t in range(array_sum, -1, -1):
            if t >= num and mat[t - num] == 1:
                mat[t] = 1

        if mat[target] == 1:
            return True

    return False

# TLE
def canPartition(self, nums: List[int]) -> bool:
        
    total = sum(nums)
    
    if total % 2 != 0: return False
    target = total // 2
    
    @lru_cache
    def search(i, curr_sum):
        if i >= len(nums) or curr_sum > target: return False
        if curr_sum == target: return True
        return search(i + 1, curr_sum + nums[i]) or search(i + 1, curr_sum)
    
    return search(0, 0)

# 0-1 knapsack
def canPartition(self, nums: List[int]) -> bool:
        
    sums = sum(nums)
    if sums % 2 != 0: return False
    
    target = sums // 2
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = True
    
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] = dp[i - 1][j] or (nums[i - 1] <= j and dp[i - 1][j - nums[i - 1]])
    
    return dp[-1][-1]