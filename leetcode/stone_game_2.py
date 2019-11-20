# Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

 

# Example 1:

# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

# Constraints:

# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4

def stoneGameII(self, piles: List[int]) -> int:
        
    cache = {}
    def traverse(i, M, max_turn):
        if i >= len(piles): return 0
        if (i, M, max_turn) in cache: return cache[i, M, max_turn] 
        
        sums = 0
        if max_turn:
            res = -float('inf')
            for t in range(min(2 * M, len(piles) - i)):
                sums += piles[i + t]
                res = max(res, sums + traverse(i + t + 1, max(M, t + 1), False))
        else:
            res = float('inf')
            for t in range(min(2 * M, len(piles) - i)):
                res = min(res, traverse(i + t + 1, max(M, t + 1), True))
                
        cache[i, M, max_turn] = res
        return res
    
    return traverse(0, 1, True)