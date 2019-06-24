# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None 


def list_of_depths(root):

    if not root: return 

    stack = [(root, 0)]
    lis = []

    while stack:
        node, level = stack.pop(0)

        if len(lis) == level:
            lis.append([ListNode(node.val)])
        else:
            lis[level].append(ListNode(node.val))
            lis[level][-2].next = lis[level][-1]

        if node.left: stack.append((node.left, level + 1))
        if node.right: stack.append((node.right, level + 1))

    return [i[0] for i in lis]

