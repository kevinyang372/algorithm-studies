# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:

# Input: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

cache = {}

def rob(root):
    if not root: return 0
    if root in cache: return cache[root]

    rob = root.val
    notrob = 0

    if root.right:
        rob += rob(root.right.right) + rob(root.right.left)
        notrob += rob(root.right)

    if root.left:
        rob += rob(root.left.right) + rob(root.left.left)
        notrob += rob(root.left)

    res = max(rob, notrob)
    cache[root] = res
    return res

# recursive
def rob(self, root: TreeNode) -> int:
        
    @lru_cache
    def search(node, could_rob):
        if not node: return 0
        curr = 0
        
        if could_rob:
            curr = node.val
            return max(curr + search(node.right, False) + search(node.left, False), search(node.right, True) + search(node.left, True))
        
        return search(node.right, True) + search(node.left, True)
    
    return search(root, True)