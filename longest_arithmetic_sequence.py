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


def lengthOfLAS(nums):

    LAS = [1] + [2 for t in range(1, len(nums))]
    LAS_val = [None] + [[nums[t] - nums[0]] for t in range(1, len(nums))]

    for i in range(1, len(nums)):
        for j in range(1, i):
            if nums[i] - nums[j] in LAS_val[j]:
                if LAS[i] == LAS[j] + 1:
                    LAS_val[i].append(nums[i] - nums[j])
                elif LAS[i] < LAS[j] + 1:
                    LAS[i] = LAS[j] + 1
                    LAS_val[i] = [nums[i] - nums[j]]
            elif LAS[i] == 2:
                LAS_val[i].append(nums[i] - nums[j])

    return max(LAS)

# concise solution using dictionary

def longestArithSeqLength(self, A):
    if not A: return 0
    
    mat = {}
    
    for i in range(1, len(A)):
        for t in range(i):
            mat[i, A[i] - A[t]] = mat.get((t, A[i] - A[t]), 1) + 1
                
    return max(mat.values())

