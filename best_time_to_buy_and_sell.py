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

# O(N) Time and O(N) Space
def maxProfit(prices):

    if len(prices) < 2: return 0

    max_p = [0] * len(prices)
    max_p[-1] = prices[-1]

    for i in reversed(range(len(prices) - 1)):
        max_p[i] = max(max_p[i + 1], prices[i])

    res = 0
    for k, v in enumerate(prices):
        res = max(res, max_p[k] - v)

    return res

# O(N) Time and O(1) Space
def maxProfit(prices):

    max_profit, min_price = 0, float('inf')

    for i in prices:
        min_price = min(i, min_price)
        max_profit = max(max_profit, i - min_price)

    return max_profit


