# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# A subarray is a contiguous subsequence of the array.

# Return the length of the shortest subarray to remove.

 

# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.
# Example 4:

# Input: arr = [1]
# Output: 0
 

# Constraints:

# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9

def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    front = []
    
    for num in arr:
        if not front or front[-1] <= num:
            front.append(num)
        else:
            break
            
    tail = []
    for i in range(len(arr) - 1, -1, -1):
        if not tail or tail[-1] >= arr[i]:
            tail.append(arr[i])
        else:
            break
            
    if len(tail) + len(front) > len(arr): return 0
    
    middle = len(arr) - len(tail) - len(front)
    tail.reverse()
    res = len(arr) - max(len(tail), len(front))
    
    for i, v in enumerate(front):
        ind = bisect.bisect_left(tail, v)
        res = min(res, len(arr) - (i + len(tail) - ind + 1))
    
    return res