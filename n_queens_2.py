# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example:

# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

def totalNQueens(n):
    return len(search(0, n, []))

def search(n0, n1, pre):

    if n0 >= n1: return [pre]

    res = []

    for m in range(n1):
        check = True
        for x, y in pre:
            if abs(x - n0) == abs(y - m) or x == n0 or y == m:
                check = False
                break

        if check:
            res += search(n0 + 1, n1, pre + [[n0, m]])

    return res
