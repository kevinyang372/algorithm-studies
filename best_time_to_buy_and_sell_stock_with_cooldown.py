# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

def maxProfit(prices):

    if len(prices) < 2:
        return 0

    matrix = [[0 for _ in range(len(prices))] for _ in range(len(prices))]

    for p in range(len(prices)):

        matrix[p][p] = prices[p]

        for t in range(p):

            matrix[t][p] = matrix[p][p] - matrix[t][t]

    return find_max(matrix)


def find_max(matrix):

    max_num = float("-inf")

    for i in range(1, len(matrix)):

        temp = max([matrix[t][i] for t in range(i)] + [0])

        if i < len(matrix) - 3:
            rest = [matrix[m][i + 2:] for m in range(i + 2, len(matrix))]
            temp += find_max(rest)


        max_num = max(max_num, temp)

    return max_num