# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.

def eight_queen(num, placed = []):

    if num == 0: return [[]]

    res = []

    for m in range(8):
        if isvalid(num - 1, m, placed):
            temp = eight_queen(num - 1, placed + [(num - 1, m)])

            if temp:
                for ins in temp:
                    ins.append((num - 1, m))
                res += temp

    if not res:
        return False

    return res


def isvalid(m, n, placed):

    for k in placed:
        if k[1] == n or abs(k[0] - m) == abs(k[1] - n): return False

    return True