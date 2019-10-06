# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.

# heapq solution
def kthSmallest(matrix, k):

    h = [(row[0], row, 1) for row in matrix]
    heapq.heapify(h)
    
    for _ in range(k - 1):
        v, r, i = h[0]
        if i < len(r):
            heapq.heapreplace(h, (r[i], r, i + 1))
        else:
            heapq.heappop(h)
            
    return h[0][0]