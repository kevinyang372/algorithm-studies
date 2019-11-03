# There exists exactly n! permutations of n elements. These can be totally ordered using the dictionary ordering -- define permutation p to appear before permutation q if in the first place where p and q differ in their array representations, starting from index 0, the corresponding entry for p is less than that for q. For example, <2, 0, 1> < <2, 1, 0>

# Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array. For example, if the input is <1, 0, 3, 2> your function should return <1, 2, 0, 3>. If the input is <3, 2, 1, 0>, return <>

import bisect

# O(N) time O(N) space
def nextPermutation(p):

    i = len(p) - 1
    stack = [p[i]]

    while i > 0:
        if p[i - 1] < stack[-1]:
            ind = bisect.bisect_right(stack, p[i - 1])
            p[i - 1], stack[ind] = stack[ind], p[i - 1]
            return p[:i] + stack
        else:
            stack.append(p[i - 1])
            i -= 1

    return 