# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):

    if not root: return None

    stack = [(root, 0)]
    pre = None
    counter = 0

    while stack:

        node, level = stack.pop(0)

        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))

        if level > counter:
            node.next = None
            counter += 1
        else:
            node.next = pre
        
        pre = node
            
    return root



