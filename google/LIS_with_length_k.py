# Given an int array nums of length n and an int k. Return an increasing subsequence of length k.

# Example 1:

# Input: nums = [10, 1, 4, 8, 2, 9], k = 3
# Output: [1, 4, 8] or [1, 4, 9] or [1, 8, 9]
# Example 2:

# Input: nums = [1, 4, 8, 2, 9], k = 4
# Output: [1, 4, 8, 9]
# Expected time complexity O(nlogk).

import bisect
import collections

def lengthK(nums, k):

    if k < 1 or not nums: return []

    d = [0] * k
    c = collections.defaultdict(list)
    size = 0

    for ind, x in enumerate(nums):
        i = bisect.bisect_left(d[:size], x)
        d[i] = x
        c[i].append(ind)
        size = max(size, i + 1)

        if size == k:
            res = [nums[min(c[m])] for m in range(i)]
            return res

    return -1

