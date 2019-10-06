# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 



 

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

# Example:

# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
 

# Note:

# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.

# straightforward solution using Counter; TLE
def knightProbability(self, N, K, r, c):
        
    stack = collections.Counter([(r,c)])
    all_possibilities = 8 ** K
    
    while K:
        temp = collections.Counter()
        for x, y in stack:
            count = stack[x, y]
            m = collections.Counter()
            for dx, dy in [(-2, -1), (-1, -2), (1, -2), 
                       (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    m[x + dx, y + dy] += count
            temp += m
        stack = temp
        K -= 1
    
    total = sum([stack[x, y] for x, y in stack])
    prob = 1.0 * total / all_possibilities
    return prob

# dp
def knightProbability(self, N, K, r, c):
        
    dp = [[0] * N for _ in xrange(N)]
    dp[r][c] = 1
    for _ in xrange(K):
        dp2 = [[0] * N for _ in xrange(N)]
        for r, row in enumerate(dp):
            for c, val in enumerate(row):
                for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                               (1,2),(1,-2),(-1,2),(-1,-2)):
                    if 0 <= r + dr < N and 0 <= c + dc < N:
                        dp2[r+dr][c+dc] += val / 8.0
        dp = dp2

    return sum(map(sum, dp))