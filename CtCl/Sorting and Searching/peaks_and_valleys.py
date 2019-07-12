# Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array {S, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {S, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
# SOLUTION
# EXAMPLE
# Input: {S, 3, 1,2, 3} Output: {S, 1,3,2, 3}

# O(nlogn)
def peakValley(n):

    n = sorted(n)
    res = []

    i, j = 0, len(n) // 2

    while j < len(n) and i < len(n) // 2:
        res.append(n[j])
        res.append(n[i])

        j += 1
        i += 1

    if j < len(n):
        res.append(n[j])
    elif i < len(n) // 2:
        res.append(n[i])

    return res

# O(n)
def peakValley_d(n):

    i = 1
    
    while i < len(n) - 1:

        if n[i] > max(n[i - 1], n[i + 1]):
            i += 2
        else:
            if n[i - 1] > n[i + 1]:
                n[i - 1], n[i] = n[i], n[i - 1]
            else:
                n[i + 1], n[i] = n[i], n[i + 1]
            i += 2

    return n