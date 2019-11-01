# Given a list of Coordinates (x, y) in a 2D Matrix, get two points that have the closest Manhattan Distance.

# O(N^2)
def closestPair(coordinates):
    return min([abs(x1 - x2) + abs(y1 - y2) for x1, y1 in coordinates for x2, y2 in coordinates if x1 != x2 and y1 != y2])

