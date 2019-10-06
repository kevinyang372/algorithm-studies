# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.

def findMinDifference(self, timePoints):
        
    def transform(s):
        return int(s.split(':')[0]) * 60 + int(s.split(':')[1])
    
    maximum = 60 * 24
    time = sorted(map(transform, timePoints))
    min_diff = float('inf')
    
    for m in range(1, len(time)):
        min_diff = min(min_diff, time[m] - time[m - 1])
    
    min_diff = min(min_diff, maximum + time[0] - time[-1])
    return min_diff