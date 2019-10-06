# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element at index i to val.

# Example:

# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:

# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.


# Using Segment Tree
class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.sum = val
        self.left = None
        self.right = None
        
    def updateTree(self, index, val):
        if self.start == self.end == index:
            self.sum = val
            return
        
        mid = (self.start + self.end) // 2
        
        if index <= mid:
            self.left.updateTree(index, val)
        else:
            self.right.updateTree(index, val)
        
        self.sum = self.left.sum + self.right.sum


class NumArray(object):

    def __init__(self, nums):
        if not nums: return
        self.root = self.buildTree(0, len(nums) - 1, nums)
        
    
    def buildTree(self, start, end, vals):
        if start == end:
            return SegmentTreeNode(start, end, vals[start])
        
        mid = (start + end) // 2
        left = self.buildTree(start, mid, vals)
        right = self.buildTree(mid + 1, end, vals)
        
        cur = SegmentTreeNode(start, end, left.sum + right.sum)
        cur.left = left
        cur.right = right
        
        return cur
    
    
    def query(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        
        mid = (root.start + root.end) // 2
        
        if j <= mid:
            return self.query(root.left, i, j)
        elif i > mid:
            return self.query(root.right, i, j)
        else:
            return self.query(root.left, i, mid) + self.query(root.right, mid + 1, j)
        
    
    def update(self, i, val):
        self.root.updateTree(i, val)
        

    def sumRange(self, i, j):
        return self.query(self.root, i, j)