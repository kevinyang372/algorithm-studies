# Given a binary tree, compute a linked list from the leaves of the binary tree.

def createListOfLeaves(root):

    def traverse(node):
        if not node.left and not node.right:
            return ListNode(node.val)

        head_a = head_b = tail_a = tail_b = None

        if node.left:
            head_a, tail_a = traverse(node.left)

        if node.right:
            head_b, tail_b = traverse(node.right)

        if head_a and head_b:
            tail_a.next = head_b

        return head_a, tail_b

    return traverse(root)[0]