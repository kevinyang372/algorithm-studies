# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# https://leetcode.com/problems/trapping-rain-water/

def trap(height):

    if not height:
        return 0
    
    water_surface = [0 for i in range(len(height))]
    current_height = 0

    for t in range(len(height) - 1):
        if height[t] >= current_height:
            
            water_surface[t] = height[t]
            next_max = max(height[t + 1:])

            if height[t] <= next_max:
                current_height = water_surface[t]
            else:
                current_height = next_max
        else:
            water_surface[t] = current_height

    water_surface[-1] = height[-1]

    return sum([water_surface[i] - height[i] for i in range(len(height))])