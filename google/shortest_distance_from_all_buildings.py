# Given an office space layout in form of grid, where grid value E represents employee, X represents a wall & _ represents an empty space. We have to place a kitchen in one such empty space such that it is optimal for every employee to reach. Each Employee can move in 4 directions, Input is always valid.

#  _ , _ , _ , _ , _ , _ 
#  E , X , _ , X , E , _
#  _ , X , _ , _ , X , _ 
#  _ , _ , _ , X , X,  E 

import collections

def shortestDistance(grid):

    employee = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                employee.append((i, j))

    stack = [[(x, y)] for x, y in employee]
    visited = [set() for _ in employee]

    while stack:
        for ind, val in enumerate(stack):
            temp = []
            for x, y in val:
                visited[ind].add((x, y))
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != 'X' and (x + dx, y + dy) not in visited[ind]:
                        temp.append((x + dx, y + dy))
            stack[ind] = temp

        m = visited[0]
        for v in visited[1:]:
            if not m:
                break
            m = m.intersection(v)

        if m: return list(m)


