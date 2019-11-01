# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

# Rules for a valid pattern:

# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.
 


 

# Explanation:

# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.

# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.

# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

# Example:

# Input: m = 1, n = 1
# Output: 9

def numberOfPatterns(self, m, n):
        
    board = set([i for i in range(1, 10)])
    
    def middles(a, b):
        x, y = a - 1, b - 1
        if x // 3 == y // 3:
            if abs(x % 3 - y % 3) > 1:
                return x // 3 * 3 + (x % 3 + y % 3) // 2 + 1
            else:
                return
        elif x % 3 == y % 3:
            if abs(x // 3 - y // 3) > 1:
                return (x // 3 + y // 3) // 2 * 3 + (x % 3) + 1
            else:
                return
        elif abs(x // 3 - y // 3) > 1 and abs(x % 3 - y % 3) > 1:
            return (x // 3 + y // 3) // 2 * 3 + (x % 3 + y % 3) // 2 + 1
        return
    
    def dfs(prev, visited):
        if len(visited) > n: 
            return 0
        if len(visited) >= m:
            res = 1
        else:
            res = 0
            
        visited.add(prev)
        nextMove = board - visited
        
        for i in nextMove:
            if middles(prev, i) in visited:
                res += dfs(i, set(visited))
        
        return res
    
    sums = 0    
    for i in board:
        sums += dfs(i, set([None]))
        
    return sums