# Given number M and N intervals in the form [a, b] (inclusive) where for every interval -M <= a <= b <= M, create a program that returns a point where the maximum number of intervals overlap.

# Example:

# M: 10
# N: 4
# Intervals:
# [-3, 5]
# [0, 2]
# [8, 10]
# [6, 7]
# A correct answer would be either 0 ,1 or 2 since those points are found where 2 intervals overlap and 2 is the maximum number of overlapping intervals.

def pointMaxOverlap(M, N):

    d = [0 for _ in range(-M, M + 1)]

    for x, y in N:
        d[x + M] += 1
        if y + M + 1 < len(d): 
            d[y + M + 1] += 1

    count = 0
    max_count = [0, 0]
    for i, v in enumerate(d):
        count += v
        if count > max_count[0]:
            max_count[0] = count
            max_count[1] = i

    return max_count[1] - M
