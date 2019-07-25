# Create a class LightString to manage a string of lights, each of which has a value 0 or 1 indicating whether it is on or off.

# class LightString {
#     public LightString(int numOfLights) {
#     }

#     /**
#     * Return if the i-th light is on or off. 
#     */
#     public boolean isOn(int i) {
#     }

#     /**
#     * Switch state (turn on if it's off, turn off if it's on) of every light in the range [start, end].
#     */
#     public void toggle(int start, int end) {
#     }
# }
# Example:

# LightString str = new LightString(5); // all lights are initially off
# str.isOn(0); // false
# str.isOn(1); // false
# str.isOn(2); // false
# str.toggle(0, 2);
# str.isOn(0); // true
# str.isOn(1); // true
# str.isOn(2); // true
# str.isOn(3); // false
# str.toggle(1, 3);
# str.isOn(1); // false
# str.isOn(2); // false
# str.isOn(3); // true
# Follow-up
# Can you do better than O(n) for update?

# class LightString:

#     def __init__(self, num):
#         self.light = [0] * num

#     def isOn(self, x):
#         return self.light[x] == 1

#     def toggle(self, start, end):

#         for i in range(start, end + 1):
#             self.light[i] ^= 1

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
            self.sum += val
            return

        mid = (self.start + self.end) // 2

        if index <= mid:
            self.left.updateTree(index, val)
        else:
            self.right.updateTree(index, val)

        self.sum = self.left.sum + self.right.sum


class LightString:

    def __init__(self, num):
        self.root = self.buildTree(0, num, [0] * (num + 1))

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

    def toggle(self, start, end):
        self.root.updateTree(start, 1)
        self.root.updateTree(end + 1, -1)

    def isOn(self, x):
        return self.query(self.root, 0, x) % 2 != 0


