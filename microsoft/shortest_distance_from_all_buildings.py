# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# Example:

# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# Output: 7 

# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total 
#              travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

# bfs TLE
def shortestDistance(self, grid):
    to_visit = set()
    available = []
    for i in range(len(grid)):
        for t in range(len(grid[0])):
            if grid[i][t] == 0:
                available.append([i, t])
            elif grid[i][t] == 1:
                to_visit.add((i, t))

    def bfs(start, targets):
        sums = 0
        queue = collections.deque([(start[0], start[1], 0)])
        visited = set()

        while queue and targets:
            x, y, steps = queue.popleft()
            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != 2 and (x + dx, y + dy) not in visited:
                    if (x + dx, y + dy) in targets:
                        sums += steps + 1
                        targets.remove((x + dx, y + dy))
                        visited.add((x + dx, y + dy))
                    else:
                        queue.append((x + dx, y + dy, steps + 1))
                        visited.add((x + dx, y + dy))

        if len(targets) > 0:
            return float('inf')
        return sums

    min_val = float('inf')
    for loc in available:
        temp = bfs(loc, set(to_visit))
        min_val = min(temp, min_val)

    return min_val if min_val != float('inf') else -1