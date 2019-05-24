# Given an array A of integers, return the length of the longest arithmetic subsequence in A.

# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

# Example 1:

# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.



# First Solve Longest Increasing Subsequence

def lengthOfLIS(nums):

    if len(nums) == 0:
        return 0

    LIS = [1 for t in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    return max(LIS)
