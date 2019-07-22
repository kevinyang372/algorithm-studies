# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two (axis-aligned) rectangles, return whether they overlap.

# Example 1:

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Notes:

# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.

def isRectangleOverlap(self, rec1, rec2):
    rec1_y = [rec1[1], rec1[3]]
    rec2_y = [rec2[1], rec2[3]]
    
    rec1_x = [rec1[0], rec1[2]]
    rec2_x = [rec2[0], rec2[2]]
    
    t1 = (rec1_y[0] < rec2_y[1] and rec1_y[0] >= rec2_y[0]) or (rec2_y[0] < rec1_y[1] and rec2_y[0] >= rec1_y[0])
    t2 = (rec1_x[0] < rec2_x[1] and rec1_x[0] >= rec2_x[0]) or (rec2_x[0] < rec1_x[1] and rec2_x[0] >= rec1_x[0])
    
    return t1 and t2