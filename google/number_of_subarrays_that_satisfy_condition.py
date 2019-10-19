# Given an array A that is a permutation of n numbers [1-n]. Find the number of subarrarys S that meets the following condition max(S) - min(S) = length(S) - 1.

# Example 1:

# Input: [4, 3, 1, 2, 5]
# Output: 10
# Explanation:
# subarrays that meets the condition are
# [4]
# [3]
# [1]
# [2]
# [5]
# [4 3]
# [1 2]
# [3 1 2]
# [4 3 1 2]
# [4 3 1 2 5]

def numSubarray(arr):

    res = len(set(arr))

    for m in range(len(arr) - 1):
        max_val = min_val = arr[m]
        for n in range(m + 1, len(arr)):
            max_val = max(max_val, arr[n])
            min_val = min(min_val, arr[n])

            if max_val - min_val == n - m:
                res += 1

    return res

