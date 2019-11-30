# Return any binary tree that matches the given preorder and postorder traversals.

# Values in the traversals pre and post are distinct positive integers.

 

# Example 1:

# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
 

# Note:

# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

def constructFromPrePost(self, pre, post):
    if not pre: return
    if len(pre) == 1: return TreeNode(pre[0])
    root = TreeNode(pre[0])
    left, right = post.index(pre[1]), pre.index(post[-2])
    
    if right - 1 != left + 1:
        root.left = self.constructFromPrePost(pre[1:], post[:-1])
    else:
        root.left = self.constructFromPrePost(pre[1:right], post[:left + 1])
        root.right = self.constructFromPrePost(pre[right:], post[left + 1:-1])
    
    return root