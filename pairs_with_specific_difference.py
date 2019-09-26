# Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

# Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

# Examples:

# input:  arr = [0, -1, -2, 2, 1], k = 1
# output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

# input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
# output: []

# naive sorting
def find_pairs_with_given_difference(arr, k):
    res = []
    d = {}
    for ind, val in enumerate(arr):
        if val - k in d:
            res.append([(val, val - k), d[val - k]])
        if k + val in d:
            res.append([(k + val, val), ind])
        d[val] = ind
    
    return [[x, y] for (x, y), m in sorted(res, key=lambda x: x[1])]

# two passes
def find_pairs_with_given_difference(arr, k):
    
    res = []
    d = {}

    for i in arr:
        arr[i - k] = i

    for m in arr:
        if m in d:
            res.append([m, d[m]])
    
    return res