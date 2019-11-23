# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# Example 1:

# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
 

# Example 2:

# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
 

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

# Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

# Note:

# schedule and schedule[i] are lists with lengths in range [1, 50].
# 0 <= schedule[i].start < schedule[i].end <= 10^8.
# NOTE: input types have been changed on June 17, 2019. Please reset to default code definition to get new method signature.

def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        
    if not schedule: return
    
    start = schedule[0]
    for i in range(1, len(schedule)):
        p = q = 0
        temp = []
        while p < len(schedule[i]) and q < len(start):
            if schedule[i][p].start > start[q].end:
                temp.append(start[q])
                q += 1
            elif schedule[i][p].end < start[q].start:
                temp.append(schedule[i][p])
                p += 1
            else:
                interval = Interval(min(schedule[i][p].start, start[q].start), max(schedule[i][p].end, start[q].end))
                
                p += 1
                q += 1
                
                while (p < len(schedule[i]) and schedule[i][p].start <= interval.end) or (q < len(start) and start[q].start <= interval.end):
                    if p < len(schedule[i]) and schedule[i][p].start <= interval.end:
                        interval.end = max(interval.end, schedule[i][p].end)
                        p += 1
                    elif q < len(start) and start[q].start <= interval.end:
                        interval.end = max(interval.end, start[q].end)
                        q += 1
                
                temp.append(interval)
                
        while p < len(schedule[i]):
            temp.append(schedule[i][p])
            p += 1
        
        while q < len(start):
            temp.append(start[q])
            q += 1
            
        start = temp
    
    res = []
    for t in range(1, len(start)):
        res.append(Interval(start[t - 1].end, start[t].start))
    
    return res