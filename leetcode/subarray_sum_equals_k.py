# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# this is O(N^2)
def subarraySum_slow(nums, k):

    if not nums: return 0

    matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    count = 0

    for m in range(len(nums)):
        for n in range(m, -1, -1):
            if m == n:
                matrix[m][n] = nums[m]
            else:
                matrix[m][n] = matrix[m][m] + matrix[m - 1][n]

            if matrix[m][n] == k:
                count += 1

    return count

# this is O(N)
def subarraySum(nums, k):

    d = collections.Counter()
    d[0] = 1
    s = 0
    res = 0

    for i in nums:
        s += i
        res += d[s - k]
        d[s] += 1

    return res