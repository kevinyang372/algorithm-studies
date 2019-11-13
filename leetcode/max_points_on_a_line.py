# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Example 1:

# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# Example 2:

# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6

def maxPoints(self, points):
        
    if not points: return 0
    
    c = collections.Counter([tuple(i) for i in points])
    
    def compute(p1, p2):
        if p1[0] == p2[0]:
            slope = float('inf')
            intercept = p1[0]
        else:
            slope = float(p1[1] - p2[1]) * 100 / float(p1[0] - p2[0])
            intercept = p1[1] - slope * p1[0]
        return slope, intercept
    
    d = collections.defaultdict(set)
    
    for i in range(1, len(points)):
        for j in range(i):
            k, b = compute(points[i], points[j])
            d[k, b].add(tuple(points[i]))
            d[k, b].add(tuple(points[j]))
    
    max_val = 1
    
    for i in d:
        temp = 0
        for t in d[i]:
            temp += c[t]
        max_val = max(temp, max_val)
        
    return max_val