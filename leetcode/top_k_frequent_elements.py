# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

import collections
import heapq

def topKFrequent(nums, k):

    count = collections.Counter(nums)
    max_heap = [(-val, key) for key, val in count.items()]
    heapq.heapify(max_heap)

    res = []

    for i in range(k):
        res.append(heapq.heappop(max_heap)[1])

    return res

def topKFrequent(self, nums, k):
    return [x for x, y in collections.Counter(nums).most_common(k)]


