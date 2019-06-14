# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    if len(intervals) == 0: return []

    m = 1
    while m < len(intervals):

        for n in range(m, 0, -1):
            temp = canmerge(intervals[n], intervals[n - 1])
            
            if temp:
                intervals[n - 1] = temp
                intervals.pop(n)
                m -= 2
                break
            elif intervals[n][0] < intervals[n - 1][1]:
                intervals[n], intervals[n - 1] = intervals[n - 1], intervals[n]
                
        m += 1

    return intervals


def canmerge(int1, int2):
    
    diff1 = int1[1] - int1[0]
    diff2 = int2[1] - int2[0]
    diff = abs(max(int2[1], int1[1]) - min(int1[0], int2[0]))

    if diff <= diff1 + diff2:
        return [min(int1[0], int2[0]), max(int1[1], int2[1])]

    return False