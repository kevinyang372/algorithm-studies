# Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

# Example 1:

# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: 
# We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:

# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: 
# In this case it's not possible to get a pair sum less that 15.
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000

# O(N^2)
def twoSumLessThanK(self, A, K):
        
    max_res = -1
    for i in range(len(A) - 1):
        for t in range(i + 1, len(A)):
            if A[i] + A[t] < K:
                max_res = max(max_res, A[i] + A[t])
    
    return max_res

# O(NlogN)
def twoSumLessThanK(self, A, K):
        
    if len(A) < 2: return -1
    
    A.sort()
    max_res = -1
    i, j = 0, len(A) - 1
    
    while i < j:
        sums = A[i] + A[j]
        if sums >= K:
            j -= 1
        else:
            max_res = max(sums, max_res)
            i += 1
    
    return max_res