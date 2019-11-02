# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

# Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

# Find the last number that remains starting with a list of length n.

# Example:

# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6

# Output:
# 6

# list manipulation TLE
def lastRemaining(self, n):
    l = [i for i in range(1, n + 1)]
    while len(l) > 1:
        l = l[1::2][::-1]
    return l[0]

# iterative dp
def lastRemaining(self, n):
    if n == 1: return 1
    dp = [1, n, 1]
    
    while dp[1] > 1:
        if dp[1] % 2 == 0:
            dp[0] = dp[0] + (dp[1] - 1) * dp[2]
        else:
            dp[0] = dp[0] + (dp[1] - 2) * dp[2]
        dp[1] //= 2
        dp[2] *= -2
        
    return dp[0]