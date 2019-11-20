# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:

# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
 

# Note:

# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

def findLength(self, A: List[int], B: List[int]) -> int:
        
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    max_val = 0
    
    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] == A[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_val = max(max_val, dp[i][j])
            
    return max_val