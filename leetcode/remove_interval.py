# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

# We remove the intersections between any interval in intervals and the interval toBeRemoved.

# Return a sorted list of intervals after all such removals.

 

# Example 1:

# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
# Example 2:

# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]

def removeInterval(self, intervals, toBeRemoved):
    res = []
    for x, y in intervals:
        if y <= toBeRemoved[0]:
            res.append([x, y])
        elif x >= toBeRemoved[1]:
            res.append([x, y])
        elif x < toBeRemoved[0] and toBeRemoved[0] < y <= toBeRemoved[1]:
            res.append([x, toBeRemoved[0]])
        elif x < toBeRemoved[0] and y > toBeRemoved[1]:
            res.append([x, toBeRemoved[0]])
            res.append([toBeRemoved[1], y])
        elif x < toBeRemoved[1] and y > toBeRemoved[1]:
            res.append([toBeRemoved[1], y])
            
    return res