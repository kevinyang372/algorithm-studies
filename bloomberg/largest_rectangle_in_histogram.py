# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

# hashmap O(N^2)
def largestRectangleArea(self, heights):
        
    if not heights: return 0
    
    record = {}
    max_size = 0
    
    for i in heights:
        temp = {}
        temp[i] = max(1, record.get(i, -1) + 1)
        
        for h in record:
            if h <= i:
                temp[h] = record[h] + 1
                max_size = max(temp[h] * h, max_size)
            else:
                max_size = max(record[h] * h, max_size)
                temp[i] = max(record[h] + 1, temp[i])
        
        max_size = max(max_size, temp[i] * i)
        record = temp
    
    return max_size

# divide and conquer
def largestRectangleArea(self, heights):
        
    def calculate(heights, start, end):
        if start > end: return 0
        min_ind = start
        
        for i in range(start, end + 1):
            if heights[i] < heights[min_ind]:
                min_ind = i
                
        return max(heights[min_ind] * (end - start + 1), calculate(heights, start, min_ind - 1), calculate(heights, min_ind + 1, end))
            
    return calculate(heights, 0, len(heights) - 1)