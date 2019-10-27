# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].

def findLongestChain(self, pairs):
        
    pairs.sort()
    dp = [[0, 0] for _ in range(len(pairs))]
    dp[0] = [1, pairs[0][1]]
    
    for i in range(1, len(pairs)):
        dp[i] = [1, pairs[i][1]]
        for j in range(i):
            if dp[j][1] < pairs[i][0]:
                if dp[j][0] + 1 > dp[i][0]:
                    dp[i] = [dp[j][0] + 1, pairs[i][1]]
            elif dp[j][0] > dp[i][0]:
                dp[i] = [dp[j][0], dp[j][1]]

    return dp[-1][0]