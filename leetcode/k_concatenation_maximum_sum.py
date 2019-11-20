# Given an integer array arr and an integer k, modify the array by repeating it k times.

# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

# As the answer can be very large, return the answer modulo 10^9 + 7.

 

# Example 1:

# Input: arr = [1,2], k = 3
# Output: 9
# Example 2:

# Input: arr = [1,-2,1], k = 5
# Output: 2
# Example 3:

# Input: arr = [-1,-2], k = 7
# Output: 0
 

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4

def kConcatenationMaxSum(self, arr, k):
    if sum(arr) > 0:
        top = sum(arr) * k
    else:
        top = 0
        
    running_sums = right_sums = left_sums = 0
    inner_sums = 0
    min_sums = 0

    for i in range(len(arr)):
        running_sums += arr[i]
        min_sums = min(running_sums, min_sums)
        left_sums = max(running_sums, left_sums)
        inner_sums = max(inner_sums, running_sums - min_sums)
       
    running_sums = 0
    for j in range(len(arr) - 1, -1, -1):
        running_sums += arr[j]
        right_sums = max(running_sums, right_sums)
    
    return max(top, left_sums + right_sums + max(0, (k - 2) * running_sums), inner_sums) % (10 ** 9 + 7)