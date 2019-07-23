# This was a very interesting problem to understand in the first place.

# Given a board that is a kingdom. The board is represented as an array of strings. Each string contains a number of tiles separated by a space. Each tile consists of a letter, and there can be 0-9 crowns. Your task is to calculate the total score. The score calculation is done by using the following formula:
# number of same tiles in an area * number of crowns in that area.

# A board can be of any size no greater than 5x5.

# Example:



# Input:
# ["L0 W1 W1 W0 F2",
# "W0 W0 T0 T0 T0",
# "W0 W1 T0 R2 R1" ,
# "L0 K0 L1 L0 L0",
# "R0 C2 C0 L1 T0"]

# Output: 41

# Explanation: The total score of this board is 41.
# (1 * 0) + (7 * 3) + (1 * 2) + (4 * 0) + (2 * 3) + (1 * 0) + (4 * 2) + (1 * 0) + (2 * 2) + (1 * 0) = 0 + 21 + 2 + 0 + 6 + 0 + 8 + 0 + 4 + 0 = 41.

def boardScore(inp):

    board = [[(t[0], int(t[1])) for t in i.split(' ')] for i in inp]

    def bfs(x, y, key):

        count = board[x][y][1]
        area = 1
        board[x][y] = (None, None)

        for (p1, p2) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if x + p1 >= 0 and x + p1 < len(board) and y + p2 >= 0 and y + p2 < len(board[0]) and board[x + p1][y + p2][0] == key:
                a, c = bfs(x + p1, y + p2, key)
                area += a
                count += c

        return area, count

    total = 0
    for i in range(len(board)):
        for t in range(len(board[0])):
            if board[i][t][0]:
                a, c = bfs(i, t, board[i][t][0])
                total += a * c

    return total