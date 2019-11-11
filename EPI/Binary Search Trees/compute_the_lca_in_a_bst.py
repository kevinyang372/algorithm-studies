def findLCA(root, n1, n2):
    if (root.val - n1.val) * (root.val - n2.val) <= 0:
        return root
    elif root.val > n1.val:
        return self.findLCA(root.left, n1, n2)
    else:
        return self.findLCA(root.right, n1, n2)