# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

def getRow(rowIndex):

    if rowIndex == 0:
        return [1]

    base = []
    res = getRow(rowIndex - 1)

    for i in range(1, len(res)):
        base.append(res[i - 1] + res[i])

    base = [1] + base + [1]

    return base
