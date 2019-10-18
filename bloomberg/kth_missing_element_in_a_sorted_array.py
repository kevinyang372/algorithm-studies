# Find the kth missing element in a sorted array.

# Example 1:

# Input: [1, 3, 5, 6, 8, 10], k = 3
# Output: 7
# Example 2:

# Input: [1, 2, 3, 4, 5], k = 2
# Output: 7

def kthMissing(arr, k):

    lower, upper = 0, len(arr)

    while lower < upper:
        mid = (lower + upper) // 2

        if arr[mid] > mid + k + 1:
            upper = mid
        else:
            lower = mid + 1
          
    while arr[mid] == mid + k + 1:
        mid -= 1

    return mid + k + 1