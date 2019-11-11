# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def combine(self, n, k):
    if k == 1: return [[i] for i in range(1, n + 1)]
    res = []
    for i in range(k, n + 1):
        res += [c + [i] for c in self.combine(i - 1, k - 1)]
    return res