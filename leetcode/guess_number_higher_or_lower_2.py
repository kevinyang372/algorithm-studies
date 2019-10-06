# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

# Example:

# n = 10, I pick 8.

# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.

# Game over. 8 is the number I picked.

# You end up paying $5 + $7 + $9 = $21.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

def getMoneyAmount(self, n):
    if n < 2: return 0
    
    cache = {}
    def guess(lower, upper):
        if (lower, upper) in cache: return cache[lower, upper]
        if lower >= upper: return 0
        
        res = min([i + max(guess(lower, i - 1), guess(i + 1, upper)) for i in range(lower, upper + 1)])
        cache[lower, upper] = res
        
        return res
    
    return guess(1, n)