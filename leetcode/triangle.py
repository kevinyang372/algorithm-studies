# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


def minimumTotal(triangle):

    tab = [[None for i in range(len(triangle))] for t in range(len(triangle))]

    tab[0][0] = triangle[0][0]

    for m in range(1, len(triangle)):
        for n in range(m + 1):
            if n == 0:
                tab[m][n] = triangle[m][n] + tab[m - 1][n]
            elif n == m:
                tab[m][n] = triangle[m][n] + tab[m - 1][n - 1]
            else:
                tab[m][n] = min(triangle[m][n] + tab[m - 1][n], triangle[m][n] + tab[m - 1][n - 1])

    minimum = tab[len(triangle) - 1][0]

    for i in range(1, len(triangle)):
        minimum = min(minimum, tab[len(triangle) - 1][i])

    return minimum


# Three line solution
def minimumTotal(triangle):
    last = triangle[-1]
    for d in range(len(triangle)-2,-1,-1):
        last = [triangle[d][i] + min(last[i], last[i+1]) for i in range(d+1)]
    return last[0]

