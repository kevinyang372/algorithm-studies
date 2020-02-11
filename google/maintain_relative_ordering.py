# You are given an array A of distinct integers, you have to return another array B which transforms the first array such that the minimum element in the new array is 1 and all the other elements maintain their relative ordering i.e. if A[i] > A[j] then it should also be that B[i] > B[j] and similarly for other elements. Also, the maximum number in B should be minimized. Better explanation of this question can be found here.

# Input: [4, 2, 3, 7] 
# Output: [3, 1, 2, 4]

# Input: [-4, -2, -3, -7] 
# Output: [2, 4, 3, 1]

def relativeOrdering(arr):
    reference = {v:i + 1 for i, v in enumerate(list(set(arr)))}
    return [reference[num] for num in arr]

# Follow ups:

# What if the elements are not distinct?
# Second question: You have to perform the same operation on a 2D array of distinct elements. The ranking should hold for within each row and each column only.
# What if the matrix has duplicates?
# Input:
# 1 5 6
# 4 3 2
# 8 7 9

# Output:
# 1 3 4
# 3 2 1
# 5 4 6