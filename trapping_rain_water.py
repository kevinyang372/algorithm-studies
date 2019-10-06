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

# TLE
def trap(self, height):
        
    d = collections.defaultdict(int)
    res = 0
    
    for i, v in enumerate(height):
        for m in range(v + 1):
            if m in d:
                res += i - d[m] - 1
            d[m] = i
    
    return res

# dp
def trap(self, height):
        
    left_max, right_max = [], []
    
    cur_max = -float('inf')
    for i in range(len(height)):
        cur_max = max(height[i], cur_max)
        left_max.append(cur_max)
    
    cur_max = -float('inf')
    for i in range(len(height) - 1, -1, -1):
        cur_max = max(height[i], cur_max)
        right_max.append(cur_max)

    ans = 0
    for i in range(len(height)):
        ans += min(left_max[i], right_max[len(height) - i - 1]) - height[i]
    
    return ans