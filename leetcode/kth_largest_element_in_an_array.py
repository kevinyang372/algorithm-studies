# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

import heapq

def findKthLargest(nums, k):

    if not nums: return None

    temp = [i * -1 for i in nums]
    heapq.heapify(temp)
    res = 0

    for i in range(k):
        res = heapq.heappop(temp)

    return -res


def findKthLargest(self, nums: List[int], k: int) -> int:
        
    def select(arr, k):
        pivot = arr[0]
        
        left, middle, right = [], [], []
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                left.append(i)
        
        if len(right) >= k:
            return select(right, k)
        elif len(right) + len(middle) >= k:
            return pivot
        else:
            return select(left, k - len(right) - len(middle))
            
    return select(nums, k)

