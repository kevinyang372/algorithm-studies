# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10] 
# Output: 1

def change(amount, coins):

    if amount < min(coins):
        return []

    result = []

    if amount in coins:
        result.append([amount])

    for i in coins:
        temp = change(amount - i, coins)

        if temp:
            result += [sorted(t + [i]) for t in temp]

    result = sorted(result)

    return [result[i] for i in range(len(result)) if result[i] != result[i - 1]] if len(result) > 1 else result



