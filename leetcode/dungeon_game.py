# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

# -2 (K)  -3  3
# -5  -10 1
# 10  30  -5 (P)
 

# Note:

# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

# TLE dp
def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    dp = [[[] for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
    dp[0][0].append([dungeon[0][0], dungeon[0][0]])
    
    for i in range(len(dungeon)):
        for j in range(len(dungeon[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                cur = dp[i][j - 1][0][1] + dungeon[i][j]
                dp[i][j].append([min(cur, dp[i][j - 1][0][0]), cur])
            elif j == 0:
                cur = dp[i - 1][j][0][1] + dungeon[i][j]
                dp[i][j].append([min(cur, dp[i - 1][j][0][0]), cur])
            else:
                for di, dj in [[0, -1], [-1, 0]]:
                    for min_val, temp in dp[i + di][j + dj]:
                        cur = temp + dungeon[i][j]
                        res = [min(min_val, cur), cur]

                        while dp[i][j] and dp[i][j][-1][0] <= res[0] and dp[i][j][-1][1] <= res[1]:
                            dp[i][j].pop()

                        if dp[i][j] and dp[i][j][-1] >= res[0] and dp[i][j][-1][1] >= res[1]:
                            continue
                        else:
                            dp[i][j].append([min(min_val, cur), cur])
    
    res = max([i[0] for i in dp[-1][-1]])
    return max(-res + 1, 1)