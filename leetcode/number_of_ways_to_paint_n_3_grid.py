# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

# You are given n the number of rows of the grid.

# Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

# Example 1:

# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown:

# Example 2:

# Input: n = 2
# Output: 54
# Example 3:

# Input: n = 3
# Output: 246
# Example 4:

# Input: n = 7
# Output: 106494
# Example 5:

# Input: n = 5000
# Output: 30228214
 

# Constraints:

# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000

def numOfWays(self, n: int) -> int:
        
    def find_valid(a, b, c):
        res = set()
        for color in pool - set([a]):
            for next_color in pool - set([b, color]):
                for fin_color in pool - set([next_color, c]):
                    res.add((color, next_color, fin_color))
        return res
    
    dp = {}
    pool = set([0, 1, 2])
    
    for color in pool:
        for next_color in pool - set([color]):
            for fin_color in pool - set([next_color]):
                dp[color, next_color, fin_color] = 1
    
    for _ in range(2, n + 1):
        d = {}
        for config in dp:
            a, b, c = config
            num = dp[config]
            
            for res in find_valid(a, b, c):
                if res in d:
                    d[res] += num
                else:
                    d[res] = num
        dp = d
        
    return sum(v for i, v in dp.items()) % (10 ** 9 + 7)