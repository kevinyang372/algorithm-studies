# Given the coordinates of four points in 2D space, return whether the four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array with two integers.

# Example:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
 

# Note:

# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.

def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    points = [p1, p2, p3, p4]
    
    x_1, y_1 = points[0]
    for n1 in range(1, len(points)):
        x_2, y_2 = points[n1]
        
        dx, dy = abs(x_1 - x_2), abs(y_1 - y_2)
        
        if dx == 0 and dy == 0: return False
        
        possible_points = [(x_2 - dy, y_2 + dx), (x_2 + dy, y_2 - dx)]
        
        for n2 in range(1, len(points)):
            if n2 != n1 and (points[n2][0], points[n2][1]) in possible_points:
                x_3, y_3 = points[n2]
                
                if (x_3, y_3) == possible_points[0]:
                    x_4, y_4 = x_1 - dy, y_1 + dx
                else:
                    x_4, y_4 = x_1 + dy, y_1 - dx
                
                for n3 in range(1, len(points)):
                    if n3 != n2 and n3 != n1 and points[n3] == [x_4, y_4]:
                        return True
        
    return False