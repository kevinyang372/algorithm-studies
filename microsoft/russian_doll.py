# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:

# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# O(N^2) TLE
def maxEnvelopes(self, envelopes):
    if not envelopes: return 0
    
    envelopes.sort()
    dp = [1] * len(envelopes)
    max_val = 1
    
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])
        max_val = max(max_val, dp[i])
        
    return max_val