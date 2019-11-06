# Given a tree with parent pointers print inorder traversal without any extra space (recursion not allowed). Consise and bug free implementation required.

def inorderTraversal(root):

    res = []
    prev = None

    while root:
        if root.left and prev != root.left and prev != root.right:
            prev = root
            root = root.left
        elif root.right and prev != root.right and (prev == root.left or not root.left):
            res.append(root.val)
            prev = root
            root = root.right
        elif not root.right and not root.left:
            res.append(root.val)
            prev = root
            root = root.parent
        else:
            prev = root
            root = root.parent

    return res