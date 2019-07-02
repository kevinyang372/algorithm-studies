# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Example 1:

# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

def maxProfit(k, prices):

    if not prices: return 0

    minimum = prices[0]
    profit = 0

    for key, v in enumerate(prices):
        minimum = min(minimum, v)

        if k == 1:
            profit = max(profit, v - minimum)
        else:
            profit = max(profit, v - minimum + maxProfit(k - 1, prices[key + 1:]))

    return profit