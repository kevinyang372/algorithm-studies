# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

# backtracking
def solveNQueens(self, n):
    return self.solve(n, 0, n, [])

def solve(self, n, row, length, occupied):
    if n == 0: return []
    
    solutions = []
    for t in range(length):
        corr = True
        for x, y in occupied:
            if y == t or abs(row - x) == abs(t - y):
                corr = False
                break
        if corr:
            output = "." * t + "Q" + "." * (length - t - 1)
            if n == 1:
                solutions.append([output])
            else:
                temp = self.solve(n - 1, row + 1, length, occupied + [(row, t)])
                if temp:
                    solutions += [[output] + i for i in temp]
    return solutions