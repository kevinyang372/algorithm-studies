# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.
    
def coinChange(self, coins, amount):
    d = [-1] * (amount + 1)
    d[0] = 0
    start = min(coins)
    
    for i in range(start, len(d)):
        temp = [d[i - t] for t in coins if i >= t and d[i - t] >= 0]
        if temp:
            d[i] = min(temp) + 1
    
    return d[-1]