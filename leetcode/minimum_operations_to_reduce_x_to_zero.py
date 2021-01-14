# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.


# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109

def minOperations(self, nums: List[int], x: int) -> int:
    d = {0: 0}

    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        d[curr_sum] = i + 1

    ans = float('inf')
    curr_sum = 0
    for j in range(len(nums) - 1, -1, -1):
        if x - curr_sum in d and d[x - curr_sum] <= j + 1:
            ans = min(ans, len(nums) - 1 - j + d[x - curr_sum])
        curr_sum += nums[j]

    return ans if ans != float('inf') else -1
