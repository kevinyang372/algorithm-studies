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