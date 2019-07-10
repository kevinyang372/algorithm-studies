# You are given chess board, then you have a knight. Initially knight standing at startx, starty coordinate
# Could you find the minimum movement to targetx, targety position if num of rows and columns is infinity

# startx = 0, starty = 0; value = 1
# targetx = 1, targety = 1; value = 4

# [
# [1, 2]
# [3, 4]
# [5, 6]
# ]

# num rows and columns should be infinity 

# *********
# ***S*****
# ****T****
# *********
# *********
# *********

# single bfs
def shortestPath(start, target):

    start_stack = [[start[0], start[1], 0]]

    def bfs(stack, target):
        x, y, steps = stack.pop(0)

        if [x, y] == target:
            return steps

        for m in [1, 2]:
            n = list({1, 2} - {m})
            stack.append([x + m, y + n[0], steps + 1])
            stack.append([x - m, y - n[0], steps + 1])
            stack.append([x + m, y - n[0], steps + 1])
            stack.append([x - m, y + n[0], steps + 1])

        return False

    while True:

        temp = bfs(start_stack, target)

        if temp:
            return temp


# bidirectional bfs
def shortestPath_d(start, target):

    start_stack = [[start[0], start[1], 0]]
    target_stack = [[target[0], target[1], 0]]

    d_start = {}
    d_target = {}

    def bfs(stack, s, t):
        x, y, steps = stack.pop(0)

        if (x, y) in t:
            return steps + t[x, y]
        elif (x, y) in s:
            return False

        s[x, y] = steps

        for m in [1, 2]:
            n = list({1, 2} - {m})
            stack.append([x + m, y + n[0], steps + 1])
            stack.append([x - m, y - n[0], steps + 1])
            stack.append([x + m, y - n[0], steps + 1])
            stack.append([x - m, y + n[0], steps + 1])

        return False

    while True:

        temp = bfs(start_stack, d_start, d_target)

        if temp:
            return temp

        temp = bfs(target_stack, d_target, d_start)

        if temp:
            return temp


