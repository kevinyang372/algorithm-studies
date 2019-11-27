# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

def nextClosestTime(self, time):
        
    def allPossible(digits, pos):
        if pos == 3: return [[i] for i in digits]
        
        next = allPossible(digits, pos + 1)
        res = []
        for i in digits:
            if (pos == 0 and i > 2) or (pos == 2 and i > 5):
                continue
            for t in next:
                res.append([i] + t)
        return res
    
    digits = set([int(i) for i in time if i != ':'])
    results = allPossible(digits, 0)
    
    o1, o2 = time.split(':')
    origin = int(o1) * 60 + int(o2)
    one_day = 24 * 60
    
    min_val = [float('inf'), None]
    for n1, n2, n3, n4 in results:
        if n1 * 10 + n2 < 25:
            total = (n1 * 10 + n2) * 60 + n3 * 10 + n4
            if total > origin and total - origin < min_val[0]:
                min_val = [total - origin, "%s%s:%s%s" % (n1, n2, n3, n4)]
            elif total <= origin and total + one_day - origin < min_val[0]:
                min_val = [total + one_day - origin, "%s%s:%s%s" % (n1, n2, n3, n4)]
    return min_val[1]