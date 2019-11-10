# Design an efficient algorithm for computing (n k) which has the property that it never overflows if the final result fits in the integer word size.

def computeBinomial(n, k):
    if n < k: return -1

    s = 1
    for i in range(k + 1, n + 1):
        s *= i / (i - k)

    return s