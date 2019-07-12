# Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations. That is, implement the method track(int x), which is called when each number is generated, and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself).
# EXAMPLE
# Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3

class RankNode:
    def __init__(self, x):
        self.val = x
        self.count = 0
        self.left = None
        self.right = None
        self.left_size = 0

    def insert(self, x):
        if x == self.val:
            self.count += 1
        elif x < self.val:
            self.left_size += 1

            if not self.left:
                self.left = RankNode(x)
            else:
                self.left.insert(x)
        else:
            if not self.right:
                self.right = RankNode(x)
            else:
                self.right.insert(x)


class Stream:
    def __init__(self):
        self.total = 0
        self.root = None

    def track(self, val):
        if not self.root:
            self.root = RankNode(val)
        else:
            self.root.insert(val)

    def getRankOfNumber(self, val):

        node = self.root
        rank = 0

        while val != node.val:
            if node.val > val:
                node = node.left
            else:
                rank += node.left_size + node.count + 1
                node = node.right

        return rank + node.left_size + node.count

