# Find an element in nearly sorted array with elements slightly shuffled in a span of indices where new position is +/- 1 or 2 of correct position .
# e.g. Find element 5 where input: [3 ** 5** 4 7 11 23 51 60]. Notice the element 5 is at a location: [correct index - 1].

import bisect

def search(num, target):

    approx = bisect.bisect(num, target)

    for i in range(approx - 2, approx + 3):
        if i > 0 and i < len(num) and num[i] == target:
            return i

    return -1