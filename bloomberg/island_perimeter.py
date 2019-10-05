# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below.

import collections

def islandPerimeter(grid):
    if not grid: return 0

    start = [None, None]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start = [i, j]
                break
        if start[0]:
            break

    if start[0] is None: return 0

    stack = collections.deque([(start[0], start[1])])
    visited = set()
    res = 0

    while stack:
        x, y = stack.popleft()
        visited.add((x, y))

        count = 0
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 1:
                count += 1
                if (x + dx, y + dy) not in visited and (x + dx, y + dy) not in stack:
                    stack.append((x + dx, y + dy))

        res += 4 - count

    return res