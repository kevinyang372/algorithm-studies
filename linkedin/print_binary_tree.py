# Print a binary tree in an m*n 2D string array following these rules:

# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# Example 1:
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# Output:

# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].

def printTree(self, root: TreeNode) -> List[List[str]]:
        
    stack = [(root, 1, 1)]
    d = collections.defaultdict(dict)
    max_level = 1
    
    while stack:
        node, ind, level = stack.pop()
        max_level = max(level, max_level)
        d[level][ind] = node.val
        
        if node.left:
            stack.append((node.left, 2 * (ind - 1) + 1, level + 1))
        if node.right:
            stack.append((node.right, 2 * (ind - 1) + 2, level + 1))
            
    res = [[""] * (2 ** (max_level) - 1) for _ in range(max_level)]
    
    def traverse(level, ind, i, j):
        if level not in d or ind not in d[level]: return
        res[level - 1][(i + j) // 2] = str(d[level][ind])
        traverse(level + 1, 2 * (ind - 1) + 1, i, (i + j) // 2 - 1)
        traverse(level + 1, 2 * (ind - 1) + 2, (i + j) // 2 + 1, j)
        
    traverse(1, 1, 0, len(res[0]) - 1)
    return res