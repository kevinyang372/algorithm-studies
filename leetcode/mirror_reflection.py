# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

# Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

# Example 1:

# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

# Note:

# 1 <= p <= 1000
# 0 <= q <= p

# pure mathematical solution, doesn't work due to float point precision
def mirrorReflection(self, p: int, q: int) -> int:
    if q == 0: return 0
    start_point = (0, 0)
    slope = q / p
    
    receptors = {
        (p, 0): 0,
        (p, p): 1,
        (0, p): 2
    }
    
    def calculate_next(point, slope):
        if point in receptors: return receptors[point]
        
        x, y = point
        next_slope = -slope
        interception = y - slope * x
        
        if 0 <= interception <= p and x != 0:
            return calculate_next((0, interception), next_slope)
        elif 0 <= slope * p + interception <= p and x != p:
            return calculate_next((p, slope * p + interception), next_slope)
        elif 0 <= -interception / slope <= p and y != 0:
            return calculate_next((-interception / slope, 0), next_slope)
        elif 0 <= (p - interception) / slope <= p and y != p:
            return calculate_next(((p - interception) / slope, p), next_slope)
    
    return calculate_next(start_point, slope)

def mirrorReflection(self, p: int, q: int) -> int:
    while p % 2 == 0 and q % 2 == 0: p, q = p / 2, q / 2
    return int(1 - p % 2 + q % 2)