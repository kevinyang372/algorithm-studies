# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

# Since the answer may be large, return the answer modulo 10^9 + 7.

 

# Example 1:

# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

# Note:

# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000

def sumSubarrayMins(self, A):
    dp = [[0, 0] for _ in range(len(A))]
    res = 0
    
    stack = []
    for i in range(len(A)):
        while stack and stack[-1][0] > A[i]:
            _, ind = stack.pop()
            dp[ind][1] = i - ind - 1
        stack.append((A[i], i))
    
    while stack:
        _, ind = stack.pop()
        dp[ind][1] = len(A) - ind - 1
    
    stack = []
    for i in range(len(A) - 1, -1, -1):
        while stack and stack[-1][0] >= A[i]:
            _, ind = stack.pop()
            dp[ind][0] = ind - i - 1
        stack.append((A[i], i))
    
    while stack:
        _, ind = stack.pop()
        dp[ind][0] = ind
    
    for i, (x, y) in enumerate(dp):
        res += A[i] * (x + 1) * (y + 1)
        
    return res % (10 ** 9 + 7)