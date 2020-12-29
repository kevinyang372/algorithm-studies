# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.


# Example 1:


# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 2:


# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 3:

# Input: root = [9]
# Output: 1


# Constraints:

# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.

def pseudoPalindromicPaths(self, root: TreeNode) -> int:

    def findPath(node, k):
        if not node:
            return 0
        if node.val in k: 
            k.remove(node.val)
        else:
            k.add(node.val)

        if not node.left and not node.right:
            return 1 if len(k) < 2 else 0

        return findPath(node.left, set(k)) + findPath(node.right, set(k))

    return findPath(root, set())


# no copying
def pseudoPalindromicPaths(self, root: TreeNode) -> int:
    def check_pseudo_palindrome(c):
        has_odd = 0
        for num in c:
            if c[num] % 2 == 1:
                if has_odd > 0:
                    return False
                has_odd += 1
        return True

    def traverse(node, c):
        if not node:
            return 0
        if not node.left and not node.right:
            c[node.val] += 1
            curr = 1 if check_pseudo_palindrome(c) else 0
            c[node.val] -= 1
            return curr

        c[node.val] += 1
        curr = traverse(node.left, c) + traverse(node.right, c)
        c[node.val] -= 1

        return curr

    return traverse(root, collections.Counter())
