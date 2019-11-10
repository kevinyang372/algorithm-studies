def optimalValue(weights, values, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
      
    return dp[-1][-1]