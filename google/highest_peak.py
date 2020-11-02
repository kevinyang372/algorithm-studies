# Given a 2D boolean array where true represents water and false represents land, generate a grid with highest possible peak. Rules are:

# the height of any water cell is 0.
# the height of any land cell cannot differ for more than one from any of the neighbouring (sharing one edge) cells.
# Example:

# Input:
# [[T, F, T],
#  [F, F, F],
#  [F, F, F]]

# One possible grid is
# [[0, 0, 0],
#  [1, 0, 1],
#  [2, 1, 2]]

# And grid 
# [[0, 2, 0], 
#  [0, 0, 0],
#  [0, 0, 0]]
# is not possible (2 differs more than 1 from the neighbouring cell)

# Output:  
# [[0, 1, 0],
#  [1, 2, 1],
#  [2, 3, 2]]
# where the highest peak is 3.
# Follow-up:
# What if we want to add secondary optimization goal: maximize the amount of cells with the height of 0 while keeping max peak height.

def find_highest_peak(map):
    water_grids = [(i, j) for i in range(len(map)) for j in range(len(map[0])) if map[i][j]]
    get_distance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    max_height = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if not map[i][j]:
                max_height = max(max_height, min(get_distance((i, j), (x, y)) for x, y in water_grids))

    return max_height

map = [[True, False, True],
[False, False, False],
[False, False, False]]

print(find_highest_peak(map))