# Given an int array holes where 1 means there is a mole, 0 means no mole. Find out the max number of moles you can hit with a mallet of width w.

# Example:

# Input: holes = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0], w = 5
# Output: 4
# Explanation: 0(11011)01000
# Follow-up:
# What if you have 2 mallets?

# Example:

# Input: holes = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0], w = 5
# Output: 6
# Explanation: 0(10011)0(11001)0

# O(N) time O(1) space solution
def mostMoles(holes, w):

    if w >= len(holes): return sum(holes)

    i = 0
    max_val = cur = sum(holes[i:i + w])

    while i + w <= len(holes):
        max_val = max(max_val, cur - holes[i] + holes[i + w - 1])
        i += 1

    return max_val

# follow-up: two passes
def mostMoles(holes, w):

    if w >= len(holes) / 2: return sum(holes)

    d = {}
    i = 0
    max_val = cur = sum(holes[i:i + w])

    while i <= len(holes) - 2 * w:
        d[i + w] = max_val
        max_val = max(max_val, cur - holes[i] + holes[i + w - 1])
        i += 1

    s = len(holes) - w
    temp = sum(holes[s:])
    res = 0

    while s >= w:
        res = max(res, temp + d[s])
        s -= 1
        temp = temp - holes[s + w] + holes[s]

    return res
