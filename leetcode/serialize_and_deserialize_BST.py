# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

class Codec:

    def serialize(self, root):
        if not root: return ""
        res = [str(root.val)]
        if root.left:
            res.append(self.serialize(root.left))
        if root.right:
            res.append(self.serialize(root.right))
        res = ','.join(res)
        return res


    def deserialize(self, data):

        if not data: return 
        s = data.split(',')
        
        def deserializer(s, lower, upper):
            if not s or int(s[-1]) < lower or int(s[-1]) > upper: return None
            root = int(s.pop())
            node = TreeNode(root)
            node.left = deserializer(s, lower, root)
            node.right = deserializer(s, root, upper)

            return node
        
        return deserializer(s[::-1], -float('inf'), float('inf'))