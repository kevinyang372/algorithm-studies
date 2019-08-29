# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

# 2d segment tree
class SegmentTreeNode(object):
    def __init__(self, sums, start, end):
        self.sum = sums
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MasterTreeNode(object):
    def __init__(self, node, start, end):
        self.node = node
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix:
            self.node = None
        else:
            self.node = self.buildTree2d(matrix, 0, len(matrix) - 1)
            
    def buildTree2d(self, lis, start, end):
        if start == end:
            node = self.buildTree(lis[start], 0, len(lis[start]) - 1)
            return MasterTreeNode(node, start, end)
        
        mid = (start + end) // 2
        le = self.buildTree2d(lis, start, mid)
        ri = self.buildTree2d(lis, mid + 1, end)
        copied = self.traverseTree(le.node, ri.node)
        
        node = MasterTreeNode(copied, start, end)
        node.left = le
        node.right = ri
        
        return node
        
    def traverseTree(self, node1, node2):
        if not node1 or not node2: return None
        
        cur = SegmentTreeNode(node1.sum + node2.sum, node1.start, node1.end)
        cur.left = self.traverseTree(node1.left, node2.left)
        cur.right = self.traverseTree(node1.right, node2.right)
        
        return cur
        
    def buildTree(self, lis, start, end):
        if start == end: return SegmentTreeNode(lis[start], start, end)
        
        mid = (start + end) // 2
        le = self.buildTree(lis, start, mid)
        ri = self.buildTree(lis, mid + 1, end)
        
        node = SegmentTreeNode(le.sum + ri.sum, start, end)
        node.left = le
        node.right = ri
        
        return node

    def getSum2d(self, root, col1, col2, row1, row2):
        if root.start == row1 and root.end == row2:
            return self.getSum(root.node, col1, col2)
        
        mid = (root.start + root.end) // 2
        
        if row2 <= mid:
            return self.getSum2d(root.left, col1, col2, row1, row2)
        elif row1 > mid:
            return self.getSum2d(root.right, col1, col2, row1, row2)
        else:
            return self.getSum2d(root.left, col1, col2, row1, mid) + self.getSum2d(root.right, col1, col2, mid + 1, row2)
        
    def getSum(self, root, start, end):
        if root.start == start and root.end == end: return root.sum
        
        mid = (root.start + root.end) // 2
        
        if end <= mid:
            return self.getSum(root.left, start, end)
        elif start > mid:
            return self.getSum(root.right, start, end)
        else:
            return self.getSum(root.left, start, mid) + self.getSum(root.right, mid + 1, end)
        
    def sumRegion(self, row1, col1, row2, col2):
        min_row, max_row = min(row1, row2), max(row1, row2)
        min_col, max_col = min(col1, col2), max(col1, col2)
            
        return self.getSum2d(self.node, min_col, max_col, min_row, max_row)