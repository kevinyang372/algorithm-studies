# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?

def longestMountain(self, A: List[int]) -> int:
    i = -1
    reached_peak = False
    max_len = 0
    
    for j in range(1, len(A)):
        if A[j] > A[j - 1]:
            if i >= 0 and reached_peak:
                max_len = max(max_len, j - i)
                i = j - 1
                reached_peak = False
            elif i < 0:
                i = j - 1
        elif A[j] < A[j - 1]:
            if i >= 0 and not reached_peak:
                reached_peak = True
        else:
            if i >= 0 and reached_peak and j - i >= 3 and A[j - 1] < A[j - 2]:
                max_len = max(max_len, j - i)
            i = -1
            reached_peak = False
    
    if i >= 0 and reached_peak and j + 1 - i >= 3 and A[j] < A[j - 1]:
        max_len = max(max_len, j + 1 - i)
        
    return max_len