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

cache = {}
    
def coinChange(self, coins, amount):
    if amount in cache: return cache[amount]
    if amount < min(coins): return -1
    if amount in coins: return 1

    min_num = float('inf')

    for i in coins:
        temp = coinChange(coins, amount - i)
        if temp > 0:
            min_num = min(min_num, 1 + temp)
    
    if min_num == float('inf'):
        min_num = -1
    
    cache[amount] = min_num
    
    return min_num