# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.

 

# Example 1:

# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:

# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
 

# Note:

# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.

# hash map
def minAreaRect(self, points):
    x_axis = collections.defaultdict(list)
    y_axis = collections.defaultdict(list)
    min_size = float('inf')
    
    for (x, y) in points:
        for t in x_axis[x]:
            h = abs(y - t)
            if h < min_size:
                for l in y_axis[y]:
                    if abs(l - x) * h < min_size and t in x_axis[l]:
                        min_size = abs(l - x) * h
        x_axis[x].append(y)
        y_axis[y].append(x)
    
    if min_size == float('inf'):
        return 0
    
    return min_size