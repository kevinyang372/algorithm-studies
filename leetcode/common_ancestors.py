# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
# For example, in this diagram, 6 and 8 have a common ancestor of 4.

#          14  13
#          |   |
# 1   2    4   12
#  \ /   / | \ /
#   3   5  8  9
#    \ / \     \
#     6   7     11

# parentChildPairs1 = [
#     (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
#     (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
# ]

# Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

# Sample input and output:
# hasCommonAncestor(parentChildPairs1, 3, 8) => false
# hasCommonAncestor(parentChildPairs1, 5, 8) => true
# hasCommonAncestor(parentChildPairs1, 6, 8) => true
# hasCommonAncestor(parentChildPairs1, 6, 9) => true
# hasCommonAncestor(parentChildPairs1, 1, 3) => false
# hasCommonAncestor(parentChildPairs1, 7, 11) => true
# hasCommonAncestor(parentChildPairs1, 6, 5) => true
# hasCommonAncestor(parentChildPairs1, 5, 6) => true

import collections

def hasCommonAncestor(pairs, p, q):
    d = collections.defaultdict(set)
    ind_to_ans = {}
    ancestors = []
    
    for x, y in pairs:
        if x in d:
            d[y].update(d[x])
        else:
            if y in ind_to_ans:
                ancestors[ind_to_ans[y]] = x
                ind_to_ans[x] = ind_to_ans[y]
                d[x].add(y)
            else:
                ancestors.append(x)
                ind_to_ans[x] = len(ancestors) - 1
                d[y].add(x)
                d[x].add(x)

    x_arr = set([ancestors[ind_to_ans[i]] for i in d[p]])
    y_arr = set([ancestors[ind_to_ans[i]] for i in d[q]])

    if x_arr.intersection(y_arr):
        return True
    return False