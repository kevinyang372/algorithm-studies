# In an American football game, a play can lead to 2 points (safety), 3 points (safety) or 7 points (touchdown). Many different combinations of 2, 3, and 7 point plays can make up a final score.

# Write a program that takes a final score and scores for individual plays, and return the number of combinations of plays that result in the final score.


def numberOfCombinations(num, combinations):
    dp = [[1] + [0] * num for _ in range(len(combinations))]

    for i in range(len(combinations)):
        for j in range(1, num + 1):
            with_this_play = (dp[i][j - combinations[i]]
                              if j >= combinations[i] else 0)
            without_this_play = (dp[i - 1][j] if i > 0 else 0)
            dp[i][j] = with_this_play + without_this_play

    return dp[-1][-1]
