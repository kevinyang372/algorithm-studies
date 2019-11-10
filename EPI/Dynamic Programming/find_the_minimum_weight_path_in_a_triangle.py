# Write a program that takes as input a triangle of numbers and returns the weight of a minimum weight path.

def minimumPath(triangle):

    dp = [float('inf')] * len(triangle[-1])
    dp[0] = triangle[0][0]

    for i in range(1, len(triangle)):
        temp = [float('inf')] * len(triangle[-1])
        for j in range(len(triangle[i])):
            if j == 0:
                temp[j] = dp[j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                temp[j] = dp[j - 1] + triangle[i][j]
            else:
                temp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
        dp = temp

    return min(dp)