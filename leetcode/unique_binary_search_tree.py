# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def numTrees(self, n):
        if n in self.cache: return self.cache[n]
        if n == 1 or n == 0: return 1
        res = sum([self.numTrees(i) * self.numTrees(n - i - 1) for i in range(n)])
        self.cache[n] = res
        
        return res