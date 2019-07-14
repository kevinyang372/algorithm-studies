# Return first pair of mismatching nodes (first pair as in in-order) given two pre-order traversal arrays of BSTs.

# Example 1:

# Input: pre1 = [5, 4, 2, 4, 8, 6, 9], pre2 = [5, 3, 2, 4, 8, 7, 9]
# Output: [4, 3]
# Explanation:
# Tree 1:
#      5
#   4     8
# 2  4   6  9

# Tree 2:
#      5
#   3     8
# 2  4   7  9

# inorder1 = [2, 4, 4, 5, 6, 8, 9]
# inorder2 = [2, 3, 4, 5, 7, 8, 9] 
# Example 2:

# Input: pre1 = [2, 1, 3], pre2 = [1, 2]
# Output: [3, null]
# Explanation:
# Tree 1:
#   2
# 1   3

# Tree 2:
#     1
#        2

# inorder1 = [1, 2, 3]
# inorder2 = [1, 2]
# Example 3:

# Input: pre1 = [2, 1, 3], pre2 = [1, 2, 3]
# Output: []
# Explanation:
# Tree 1:
#     2
#   1   3

# Tree 2:
#     1
#        2
#           3

# inorder1 = [1, 2, 3]
# inorder2 = [1, 2, 3]
# There is no mismatch because the in-order sequence for both is exactly the SAME, despite the trees are structurally different.

def mismatchingNode(pre1, pre2):

    ind1 = 0
    for i in range(1, len(pre1)):
        if pre1[i] <= pre1[i - 1]:
          ind1 = i
        else:
          break

    ind2 = 0
    for i in range(1, len(pre2)):
        if pre2[i] <= pre2[i - 1]:
          ind2 = i
        else:
          break

    while pre1 and pre2:

        if pre1[ind1] == pre2[ind2]:
            pre1.pop(ind1)
            pre2.pop(ind2)

            if ind1 > 0:
                ind1 = min([ind1, ind1 - 1], key = lambda x: pre1[x])

            if ind2 > 0:
                ind2 = min([ind2, ind2 - 1], key = lambda x: pre2[x])
        else:
            return [pre1[ind1], pre2[ind2]]

    if not pre1 and not pre2:
        return None
    elif not pre1:
        return [None, pre2[ind2]]
    else:
        return [pre1[ind1], None]


