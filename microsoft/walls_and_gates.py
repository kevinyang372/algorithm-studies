# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

def wallsAndGates(self, rooms):
    to_visit = []
    for i in range(len(rooms)):
        for t in range(len(rooms[0])):
            if rooms[i][t] == 0:
                to_visit.append((i, t))
        
    for x, y in to_visit:
        queue = collections.deque([(x, y, 0)])
        
        while queue:
            nx, ny, steps = queue.pop()
            visited = set([(nx, ny)])
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= nx + dx < len(rooms) and 0 <= ny + dy < len(rooms[0]) and rooms[nx + dx][ny + dy] != -1 and (nx + dx, ny + dy) not in visited and steps + 1 < rooms[nx + dx][ny + dy]:
                    rooms[nx + dx][ny + dy] = steps + 1
                    visited.add((nx + dx, ny + dy))
                    queue.append((nx + dx, ny + dy, steps + 1))
                    
    return rooms