# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

def containsNearbyAlmostDuplicate(self, lis, k, t):
    if k < 1 or not lis: return False

    if k < 2 * t:
        for i in range(1, len(lis)):
            cur = lis[i]
            for m in range(1, k + 1):
                if i - m < 0:
                    break
                if abs(lis[i - m] - cur) <= t:
                    return True
    else:
        d = {}
        for i, v in enumerate(lis):
            for dv in range(-t, t + 1):
                if v + dv in d and i - d[v + dv] <= k:
                    return True
            d[v] = i

    return False