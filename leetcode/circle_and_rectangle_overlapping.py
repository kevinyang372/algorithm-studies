# Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

# Return True if the circle and rectangle are overlapped otherwise return False.

# In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.

 

# Example 1:



# Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0) 
# Example 2:



# Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# Output: true
# Example 3:



# Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
# Output: true
# Example 4:

# Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# Output: false
 

# Constraints:

# 1 <= radius <= 2000
# -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
# x1 < x2
# y1 < y2

def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
    x3, y3, x4, y4 = x_center - radius, y_center - radius, x_center + radius, y_center + radius
    
    if x2 < x3 or y2 < y3 or x4 < x1 or y4 < y1: return False
    
    lower_x, lower_y = max(x1, x3), max(y1, y3)
    upper_x, upper_y = min(x2, x4), min(y2, y4)
    
    if (lower_x - x_center) * (upper_x - x_center) > 0 and (lower_y - y_center) * (upper_y - y_center) > 0:
        
        d1 = (lower_x - x_center) ** 2 + (lower_y - y_center) ** 2
        d2 = (upper_x - x_center) ** 2 + (upper_y - y_center) ** 2
        d3 = (lower_x - x_center) ** 2 + (upper_y - y_center) ** 2
        d4 = (upper_x - x_center) ** 2 + (lower_y - y_center) ** 2
        
        if d1 > radius ** 2 and d2 > radius ** 2 and d3 > radius ** 2 and d4 > radius ** 2:
            return False
        
    return True