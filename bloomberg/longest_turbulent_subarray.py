# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

 

# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:

# Input: [4,8,12,16]
# Output: 2
# Example 3:

# Input: [100]
# Output: 1
 

# Note:

# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9

def maxTurbulenceSize(self, A):
    max_val = 1
    i, j = 0, 1
    
    while j < len(A):
        if A[j] > A[i]:
            sign = True
        elif A[j] < A[i]:
            sign = False
        else:
            j += 1
            i += 1
            continue
            
        while j + 1 < len(A):
            if A[j] > A[j + 1] and sign:
                j += 1
                sign = False
            elif A[j] < A[j + 1] and not sign:
                j += 1
                sign = True
            else:
                break
            
        max_val = max(j - i + 1, max_val)
        i, j = j, j + 1
    
    return max_val