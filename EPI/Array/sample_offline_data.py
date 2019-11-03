# Implement an algorithm that takes as input an array of distinct elements and a size, and returns a subset of the given size of the array elements. All subsets should be qually likely. Return the result in input array itself.

import random

# O(N) time O(1) space
def offlineSample(arr, k):

    for i in range(len(arr)):
        di = random.randint(0, len(arr) - 1)
        arr[i], arr[di] = arr[di], arr[i]

    return arr[:k]