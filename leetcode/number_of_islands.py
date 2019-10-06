# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

def numIslands(grid):

    if not grid:
        return 0

    width = len(grid[0])
    height = len(grid)

    islands = [[0 for _ in range(width)] for _ in range(height)]
    counter = 1

    for m in range(height):
        for n in range(width):
            if grid[m][n] == "1" and islands[m][n] == 0:
                
                explore(m, n, islands, grid, counter)

                for i in islands:
                    print(i)

                counter += 1

    return counter - 1

def explore(m, n, islands, grid, counter):

    if grid[m][n] == "1" and islands[m][n] == 0:
        islands[m][n] = counter

        if m + 1 <  len(islands):
            explore(m + 1, n, islands, grid, counter)

        if n + 1 < len(islands[0]):
            explore(m, n + 1, islands, grid, counter)

        if m > 0:
            explore(m - 1, n, islands, grid, counter)

        if n > 0:
            explore(m, n - 1, islands, grid, counter)




