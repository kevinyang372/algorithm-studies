# Consider a binary tree in which each node contains a binary digit. A root-to_leaf path can be associated with a binary number -- the MSB is at the root.

# Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf paths.

def computeSum(root):

    def traverse(node, prev):

        sums = 0

        if not node.left and not node.right:
            return prev

        if node.left:
            sums += traverse(node.left, (prev << 1) | node.val)
        if node.right:
            sums += traverse(node.right, (prev << 1) | node.val)

        return sums

    return traverse(root, 0)