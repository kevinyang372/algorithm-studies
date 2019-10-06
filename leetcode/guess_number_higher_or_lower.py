# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example :

# Input: n = 10, pick = 6
# Output: 6

def guessNumber(self, n):
        
    i, j = 1, n + 1
    
    while i < j:
        mid = (i + j) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == 1:
            i = mid + 1
        else:
            j = mid