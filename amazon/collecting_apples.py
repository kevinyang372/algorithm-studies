# In a garden, there are several apples trees planted in a grid format. Each point (i,j) in the grid has |i| + |j| apples.

# Vijay can buy a square land centred at (0,0). Find the minimum perimeter of the land (1 unit having length = 1) such that she can collect at
# least X apples. All plants on the perimeter of the plot are also included.

# Sample:

# Input = 1 Output = 8
# input = 11 Output = 8
# Input = 13 Output = 16

def minPerimeter(num):

    available = 0
    p = 0

    while available < num:
        p += 1
        available += (sum([i for i in range(p, 2 * p + 1)]) + sum([i for i in range(2 * p - 1, p, -1)])) * 4

    return 8 * p