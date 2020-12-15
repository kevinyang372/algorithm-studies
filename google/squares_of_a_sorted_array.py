# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# Note:

# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

# Follow-up:
# Can you do it in-place (without extra array) and O(n) time?


# O(1) Space
# Time: O(logN) for binary search; O(N) for iterating through the array; 
# O(N) for popping at arbitrary index and O(N) for inserting at arbitrary index;
# Overall: O(N^2)
def sortedSquares(self, A):

    if len(A) == 1:
        return [A[0] ** 2]

    sep = bisect.bisect_left(A, 0)

    if sep == 0:
        return [n ** 2 for n in A]
    elif sep == len(A) or A[-1] == 0:
        return [n ** 2 for n in reversed(A)]

    i, j = sep - 1, sep

    while i > -1 and j < len(A):

        while j < len(A) and A[i] ** 2 > A[j] ** 2:
            A[j] = A[j] ** 2
            j += 1

        A.insert(j - 1, A.pop(i) ** 2)
        i -= 1

    print(A)
    if i > -1:
        while i > -1:
            A.insert(j - 1, A.pop(i) ** 2)
            i -= 1
    elif j < len(A):
        while j < len(A):
            A[j] = A[j] ** 2
            j += 1

    return A


# O(N) time O(N) space
def sortedSquares(self, nums: List[int]) -> List[int]:
    i = bisect.bisect_right(nums, 0) - 1
    j = i + 1

    res = []
    while i >= 0 and j < len(nums):
        if nums[i] ** 2 < nums[j] ** 2:
            res.append(nums[i] ** 2)
            i -= 1
        else:
            res.append(nums[j] ** 2)
            j += 1

    while i >= 0:
        res.append(nums[i] ** 2)
        i -= 1

    while j < len(nums):
        res.append(nums[j] ** 2)
        j += 1

    return res
