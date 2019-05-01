# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Bruteforce
def maxProfit(prices):

    if len(prices) < 2:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1] - prices[0])

    max_price = max(prices[1:])
    return max(max_price - prices[0], maxProfit(prices[1:]))

# Dynamic Programming
def maxProfit_dp(prices):

    if len(prices) < 2:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1] - prices[0])

    gaps = [[0 for i in range(len(prices) - 1)] for t in range(len(prices) - 1)]

    max_p = 0

    for p in range(len(prices) - 1):
        for t in range(len(prices) - p - 1):
            if p == 0:
                temp = prices[t + 1] - prices[t]
                max_p = max(max_p, temp)
                gaps[t][t] = temp
            else:
                temp = gaps[t][t + p - 1] + gaps[t + p][t + p]
                max_p = max(max_p, temp)
                gaps[t][t + p] = temp

    return max_p

