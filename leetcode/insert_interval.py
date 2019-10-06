# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def insert(intervals, newInterval):

    def intersect(i1, i2):
        if i1[0] <= i2[0] <= i1[1] or i2[0] <= i1[0] <= i2[1]:
            return True
        return False

    def merge(i1, i2):
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    i = 0
    while i < len(intervals):
        if intervals[i][1] < newInterval[0]:
            i += 1
        else:
            if not intersect(newInterval, intervals[i]):
                intervals.insert(i, newInterval)
                return intervals
            else:
                intervals[i] = merge(newInterval, intervals[i])
                while i < len(intervals) - 1 and intersect(intervals[i], intervals[i + 1]):
                    intervals[i] = merge(intervals[i], intervals[i + 1])
                    intervals.pop(i + 1)
                return intervals

    intervals.append(newInterval)
    return intervals