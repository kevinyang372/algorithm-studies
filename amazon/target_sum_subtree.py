# Return the root of the subtree whose sum is equal to given target (including the root value

def targetSum(root, target):

    res = []

    def search(node):

        sums = node.val
        if node.left:
            sums += search(node.left)
        if node.right:
            sums += search(node.right)

        if sums == target:
            res.append(node)

        return sums

    search(root)
    return res

        