# In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

# We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

# Return true if and only if it is possible to reach the target square through a sequence of moves.

 

# Example 1:

# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: 
# The target square is inaccessible starting from the source square, because we can't walk outside the grid.
# Example 2:

# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: 
# Because there are no blocked cells, it's possible to reach the target square.
 

# Note:

# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= blocked[i][j] < 10^6
# source.length == target.length == 2
# 0 <= source[i][j], target[i][j] < 10^6
# source != target

# bidirectional bfs TLE
def isEscapePossible(blocked, source, target):

    if not blocked: return True

    source_stack = [source]
    target_stack = [target]

    d_source = {}
    d_target = {}

    def bfs(stack, s, t):

        x, y = stack.pop(0)

        if [x, y] in blocked:
            return False
        if (x, y) in s:
            return False
        if (x, y) in t:
            return True

        s[x, y] = True

        if x > 0:
            stack.append([x - 1, y])
        if y > 0:
            stack.append([x, y - 1])
        if x < 999999:
            stack.append([x + 1, y])
        if y < 999999:
            stack.append([x, y + 1])

    while source_stack and target_stack:

        if bfs(source_stack, d_source, d_target) or bfs(target_stack, d_target, d_source):
            return True

    return False

# optimization
def isEscapePossible(blocked, source, target):

    if not blocked: return True

    blocked = {tuple(i) for i in blocked}
    seen = {tuple(source)}
    stack = [source]
    count = 0

    def bfs(stack, seen, blocked, count):
        
        node = stack.pop(0)
        count += 1

        if node == target or count >= 20000:
            return True

        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            n = (node[0] + x, node[1] + y)
            if n[0] > 0 and n[0] < 10**6 and n[1] > 0 and n[1] < 10**6 and n not in seen and n not in blocked:
                seen.add(n)
                stack.append(n)

        return False

    while True:

        if bfs(stack, seen, blocked, count):
            return True

    return False