# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):

    if len(nums) == 1:
        return nums[0]

    times_total = 1

    for i in nums:
        times_total *= i

    return max(times_total, maxProduct(nums[1:]), maxProduct(nums[:-1]))


# Dynamic Programming

def maxProduct_dp(nums):

    max_result = max(nums)
    product_sum = [[None for i in range(len(nums))] for t in range(len(nums))]

    for t in range(len(nums)):
        for row in range(len(nums) - t):
            col = row + t
            if col == row:
                product_sum[row][col] = nums[row]
                result.append(nums[row])
            else:
                temp = product_sum[col][col] * product_sum[row][col - 1]
                product_sum[row][col] = temp
                max_result = max(max_result, temp)

    return max_result

