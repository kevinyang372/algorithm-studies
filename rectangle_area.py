# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Rectangle Area

# Example:

# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Note:

# Assume that the total area is never beyond the maximum possible value of int.

def computeArea(A, B, C, D, E, F, G, H):
    r1 = (C - A) * (D - B)
    r2 = (G - E) * (H - F)
    
    r1_x = [A, C]
    r1_y = [B, D]
    
    r2_x = [E, G]
    r2_y = [F, H]
    
    overlap = check_intersection(r1_x, r2_x) * check_intersection(r1_y, r2_y)
    
    return r1 + r2 - overlap

def check_intersection(i1, i2):
    temp = min(i1[1], i2[1]) - max(i1[0], i2[0])
    return temp if temp > 0 else 0