# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example: 

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

import ast

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        
        if not root: return "[]"
        
        stack = [root]
        result = [root.val]

        while stack:
            node = stack.pop()

            le = 'null'
            ri = 'null'

            if node.right:
                stack.append(node.right)
                ri = str(node.right.val)
            if node.left:
                stack.append(node.left)
                le = str(node.left.val)

            result.append(le)
            result.append(ri)

        i = len(result) - 1
        while i > 0:
            if result[i] == 'null':
                result.pop()
            else:
                break
            i -= 1

        return "[%s]" % (','.join([str(i) for i in result]))


    def deserialize(self, data):

        data = data.replace('null', 'None')
        data = ast.literal_eval(data)

        if not data or data[0] is None: return None

        head = TreeNode(data[0])
        stack = [head]
        data = data[1:]

        while data:
            node = stack.pop()
            if len(data) < 2:
                if data[0]:
                    left = TreeNode(data[0])
                    stack.append(left)
                    node.left = left
                data = data[1:]
            else:
                if data[1] is not None:
                    right = TreeNode(data[1])
                    node.right = right
                    stack.append(right)

                if data[0] is not None:
                    left = TreeNode(data[0])
                    node.left = left
                    stack.append(left)
                
                data = data[2:]

        return head


# Optimized solution using preorder traversal
class Codec:

    def serialize(self, root):
        
        if not root: return "#"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        res = ','.join([str(root.val), left, right])
        return res


    def deserialize(self, data):

        s = data.split(',')
        
        def deserializer(s):
            # popping from tail is faster than from head
            root = s.pop()
            if root == '#': return None
            node = TreeNode(root)
            node.left = deserializer(s)
            node.right = deserializer(s)

            return node
        
        return deserializer(s[::-1])