# you are given a board with some stones placed on it, and you are given a new stone to be placed on an empty spot. you have to return the number of enemy stones that this move will capture. 

# board = [[0, 2, 2, 0, 0],[2, 1, 1, 2, 0],[2, 1, 1, 2, 0],[2, 1, 1, 0, 0],[2, 2, 2, 2, 0]]
# return 6
# [[0, 2, 0, 0, 0],[2, 1, 2, 0, 0],[2, 1, 2, 0, 0],[2, 1, 1, 0, 0],[2, 2, 2, 2, 0]]
# return 4

def search(board, x, y):

    def dfs(x, y):
        print(x, y)
        visited.add((x, y))
        to_go = []
        for di, dt in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= x + di < len(board) and 0 <= y + dt < len(board[0]):
                if board[x + di][y + dt] == 0:
                    return 0
                elif board[x + di][y + dt] == 1:
                    to_go.append((x + di, y + dt))

        sums = 1
        for i in to_go:
            if i not in visited:
                temp = dfs(i[0], i[1])
                if temp == 0:
                    return 0
                else:
                    sums += temp
        return sums

    count = 0
    board[x][y] = 2
    visited = set()

    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
            count += dfs(x + dx, y + dy)

    return count