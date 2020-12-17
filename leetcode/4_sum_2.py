# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

# Example:

# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# Output:
# 2

# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


def fourSumCount(self, A, B, C, D):

    d = collections.Counter()

    for i in A:
        for t in B:
            d[i + t] += 1

    res = 0

    for m in C:
        for n in D:
            if -m - n in d:
                res += d[-m - n]

    return res


def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

    def get_two_sum_counter(l1, l2):
        c = collections.Counter()
        c[0] = 1

        for lis in [l1, l2]:
            new_c = collections.Counter()
            for v1 in c:
                for v2 in lis:
                    new_c[v1 + v2] += c[v1]
            c = new_c

        return c

    d1 = get_two_sum_counter(A, B)
    d2 = get_two_sum_counter(C, D)
    return sum(d1[val] * d2[-val] for val in d1)
