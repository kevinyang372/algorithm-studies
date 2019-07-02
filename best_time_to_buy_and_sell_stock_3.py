# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(prices, p = 0):

    if not prices: return 0

    profit = 0
    minimum = prices[0]
    for k, v in enumerate(prices):
        if v > minimum:
            if p == 0:
                profit = max(profit, v - minimum + maxProfit(prices[k + 1:], 1))
            else:
                profit = max(profit, v - minimum)
        else:
            minimum = v

    return profit

# two passes; forward and backward traversal

def maxProfit(prices):

    if not prices: return 0

    minimum = prices[0]
    max_profit = 0
    profits = []

    for k, v in enumerate(prices):
        minimum = min(v, minimum)
        max_profit = max(max_profit, v - minimum)
        profits.append(max_profit)

    maximum = prices[-1]
    total_max = 0
    max_profit = 0

    for i in reversed(range(len(prices))):
        maximum = max(prices[i], maximum)
        max_profit = max(max_profit, maximum - prices[i])
        total_max = max(total_max, max_profit + profits[i])

    return total_max
