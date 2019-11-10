def computeDistance(s1, s2):
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + 1
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + 1
            elif s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
    return dp[-1][-1]