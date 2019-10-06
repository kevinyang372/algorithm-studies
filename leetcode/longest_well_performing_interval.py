# We are given hours, a list of the number of hours worked per day for a given employee.

# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

# Return the length of the longest well-performing interval.

 

# Example 1:

# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
 

# Constraints:

# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16

# TLE
def longestWPI(hours):
        
    d = collections.defaultdict(int)
    d[-1] = 0
    max_length = 0
    
    for i in range(len(hours)):
        temp = 1 if hours[i] > 8 else -1
        d[i] = d[i - 1] + temp
        
        for t in range(-1, i - max_length):
            if d[i] - d[t] > 0:
                max_length = max(max_length, i - t)
                break
                
    return max_length

# O(N) time
def longestWPI(hours):

    score = 0
    res = 0
    seen = {}

    for i in range(len(hours)):
        score += 1 if hours[i] > 8 else -1
        seen.setdefault(score, i)

        if score > 0: res = i + 1
        if score - 1 in seen: res = max(res, i - seen[score - 1])

    return res