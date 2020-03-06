# Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
# You may repeat this procedure as many times as needed.
# Return True if it is possible to construct the target array from A otherwise return False.

 

# Example 1:

# Input: target = [9,3,5]
# Output: true
# Explanation: Start with [1, 1, 1] 
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
# Example 2:

# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].
# Example 3:

# Input: target = [8,5]
# Output: true
 

# Constraints:

# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9

# TLE
def isPossible(self, target: List[int]) -> bool:
    
    def find_max(arr):
        max_ind = []
        for i, v in enumerate(arr):
            if not max_ind or v > arr[max_ind[0]]:
                max_ind = [i]
            elif v == arr[max_ind[0]]:
                max_ind.append(i)
        return max_ind
    
    sum_target = sum(target)
    
    while sum_target != len(target):
        
        inds = find_max(target)
        
        if len(inds) > 1: return False
        num = target[inds[0]] - (sum_target - target[inds[0]])
        
        if num < 1: return False
        target[inds[0]] = num
        sum_target = sum(target)
        
    return True

def isPossible(self, target: List[int]) -> bool:
        
    sum_target = sum(target)
    target = [-i for i in target]
    queue = heapq.heapify(target)
    
    while sum_target != len(target):
        
        max_num = -heapq.heappop(target)
        num = max_num - (sum_target - max_num)
        
        if num < 1: return False
        sum_target -= max_num - num
        heapq.heappush(target, -num)
        
    return True

def isPossible(self, target: List[int]) -> bool:
        
    target = [-i for i in target]
    queue = heapq.heapify(target)

    while True:

        sum_target = -sum(target)
        num = -heapq.heappop(target)

        if num == 1: return True
        if num < 1 or 2 * num <= sum_target or num == sum_target: return False
        
        num = num % (sum_target - num)
        heapq.heappush(target, -num)