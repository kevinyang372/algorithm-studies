# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.


def leastBricks(wall):

    wall_space = {}

    for i in range(len(wall)):
        temp_sum = 0
        for t in range(len(wall[i]) - 1):
            temp_sum += wall[i][t]

            if temp_sum in wall_space.keys():
                wall_space[temp_sum] += 1
            else:
                wall_space[temp_sum] = 1

    if not wall_space:
        return len(wall)

    return len(wall) - wall_space[max(wall_space, key=wall_space.get)]

def leastBricks(self, arr):
    d = collections.Counter()
    max_val = 0
    for i in arr:
        temp = 0
        for m in i[:-1]:
            temp += m
            d[temp] += 1
            max_val = max(max_val, d[temp])
    return len(arr) - max_val

