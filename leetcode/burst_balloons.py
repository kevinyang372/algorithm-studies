# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

def maxCoins(nums):

    if len(nums) < 2: return nums[0] if nums else 0
        
    max_num = nums[0] * nums[1] + self.maxCoins(nums[1:])

    for i in range(1, len(nums) - 1):
        max_num = max(nums[i - 1] * nums[i + 1] * nums[i] + self.maxCoins(nums[:i] + nums[i+1:]), max_num)

    max_num = max(nums[-1] * nums[-2] + self.maxCoins(nums[:-1]), max_num)

    return max_num

# dp with caching

cache = {}
    
def maxCoins(self, nums):
    if len(nums) < 2: return nums[0] if nums else 0
    if tuple(nums) in self.cache: return self.cache[tuple(nums)]
    
    max_num = nums[0] * nums[1] + self.maxCoins(nums[1:])

    for i in range(1, len(nums) - 1):
        max_num = max(nums[i - 1] * nums[i + 1] * nums[i] + self.maxCoins(nums[:i] + nums[i+1:]), max_num)

    max_num = max(nums[-1] * nums[-2] + self.maxCoins(nums[:-1]), max_num)

    self.cache[tuple(nums)] = max_num
    return max_num