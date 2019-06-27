# You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def paths_with_sum(root, target):

    running_sums = collections.defaultdict(int)
    stack = [[root, [root]]]
    res = 0

    while stack:
        
        node, path = stack.pop()

        if node.right:
            stack.append([node.right, path + [node.right]])

        if node.left:
            stack.append([node.left, path + [node.left]])

        if not node.right and not node.left:
            res += possible_paths(path, running_sums, target)

    return res

def possible_paths(path, sums, target):

    res = 0

    for k, v in path:
        if sums[v] == target:
            res += 1
        for k1, v1 in path[:k]:
            if sums[v] - sums[v1] == target:
                res += 1

    return res


